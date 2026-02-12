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
    os.system('cls')
    print('Finalizando App\n')

def opcao_invalida():
    print('Opção invalida!\n')
    input('Digite uma tecla para voltar ao menu: ')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes.')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.\n')
    input('Digite uma tecla para voltar ao meno: ')
    main()

def exolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha a opção: '))

        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
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