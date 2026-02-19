# import os

# pessoas = []

# def exibir_menu():
#     print('1. Cadastrar pessoas.')
#     print('2. Listar pessoas')
#     print('3. Atualizar idade da pessoa')
#     print('4. Remova uma pessoa.')
#     print('5. Sair do app')

# def finalizando_app():
#     os.system('cls')
#     print('Finalizando App')

# def opcao_invalida():
#     os.system('cls')
#     print('Opção invalida.\n')
#     input('Digite uma tecla para voltar ao menu: ')
#     main()

# def voltar_menu():
#     input('\nDigite uma tecla para voltar ao menu: ')
#     main()

# def pessoas_cadastro():
#     os.system('cls')
#     print('Cadastrar pessoas.')

#     nome = input('Digite seu nome: ')
#     idade = int(input(f'{nome} digite sua idade: '))
#     cidade = input(f'{nome} digite sua cidade: ')

#     dados_da_pessoa = {'nome': nome, 'idade': idade, 'cidade':cidade}
#     pessoas.append(dados_da_pessoa)

#     voltar_menu()

# def listar_pessoas():
#     os.system('cls')
#     print('Lista das pessoas.\n')

#     if len(pessoas) == 0:
#         print('Pessoas não gadastradas.')
#     else:
#         for pessoa in pessoas:
#             nome_pessoas = pessoa['nome']
#             idade_pessoa = pessoa['idade']
#             cidade_pessoa = pessoa['cidade']
#             print(f'- {nome_pessoas.ljust(20)} | {str(idade_pessoa).ljust(20)} | {cidade_pessoa}')

#     voltar_menu()

# def atualizar_idade_pessoa():
#     os.system('cls')
#     print('Atualizar Idade da pesssoa.\n')

#     atualizar_pessoa = input('Digite o nome da pessoa que você quer atualizar a idade: ')
#     encontrado = False
#     for pessoa in pessoas:
#         if atualizar_pessoa == pessoa['nome']:
#             atualizar_data = int(input('Digite a nova idade: '))
#             pessoa['idade'] = atualizar_data
#             print('Data atualizada com sucesso.')
#             encontrado = True
#     if not encontrado:
#         print('Pessoa não encontrada.')
    
#     voltar_menu()

# def remover_pessoa():
#     os.system('cls')
#     print('Remover pessoa.\n')

#     pessoa_econtrada = input('Digite a pessoa que deseja remover: ')

#     for pessoa in pessoas:
#         if pessoa_econtrada == pessoa['nome']:
#             pessoas.remove(pessoa)
#             print('Pessoa Removida com Sucesso')
#         else:
#             print('Pessoa não encontrada.')
    
#     voltar_menu()

# def escolher_opcao_menu():
#     try:
#         escolher_opcao = int(input('Escolha uma opção: '))

#         if escolher_opcao == 1:
#             pessoas_cadastro()
#         elif escolher_opcao == 2:
#             listar_pessoas()
#         elif escolher_opcao == 3:
#             atualizar_idade_pessoa()
#         elif escolher_opcao == 4:
#             remover_pessoa()
#         elif escolher_opcao == 5:
#             finalizando_app()
#         else:
#             opcao_invalida()
#     except ValueError:
#         opcao_invalida()


# def main():
#     os.system('cls')
#     exibir_menu()
#     escolher_opcao_menu()

# if __name__ == '__main__':
#     main()

# numeros_quadrados = {x: x**2 for x in range(1, 6)}
# print(numeros_quadrados)

frase = "Python se tornou uma das linguagens de programação mais populares do mundo mundo nos últimos anos."
contagem_palavras = {}
# split é um método de string que divide um texto em uma lista de substrings com base em um delimitador específico (espaço por padrão)
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
