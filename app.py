import os

restaurantes = []

def exibir_titulo():
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█""")

def exibir_menu():
    print('1.Cadastrar restaurante.')
    print('2.Listar restaurante.')
    print('3.Ativar restaurante.')
    print('4.Sair\n')

def finalizando_app():
    exibir_subtitulo('Finalizando App')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu: ')
    main()

def opcao_invalida():
    print('Opção invalida!\n')

    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes.')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.\n')

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listar os restaurantes')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria do Restaurante'.ljust(20)} | {'Status'}')
    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado.')
    else:
        # para cada restaurantes  nalista restaurantes:
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo = 'ativo' if restaurante['ativo'] else 'inativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def ativar_desativar_restaurante():
    exibir_subtitulo('Ativar e Inativar Restaurante.')

    nome_restaurante = input('Digite o nome do restaurante que deseja Ativar ou Inativar o resaturante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi inativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()

def exolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha a opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_desativar_restaurante()
        elif opcao_escolhida == 4:
            finalizando_app()   
        else:
            opcao_invalida()
    except:
        opcao_invalida()
def main():
    os.system('cls')
    exibir_titulo()
    exibir_menu()
    exolher_opcao()


if __name__ == '__main__':
    main()     