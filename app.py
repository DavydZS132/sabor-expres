import os

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

def exolher_opcao():

    opcao_escolhida = int(input('Escolha a opção: '))

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    else:
        finalizando_app()

def main():
    exibir_titulo()
    exibir_menu()
    exolher_opcao()


if __name__ == '__main__':
    main()     