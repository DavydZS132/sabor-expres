# numero = int(input('Digite um nuemro para saber se é par ou impar: '))

# if numero % 2 == 0:
#     print('O numero é par.')
# else:
#     print('Ele é impar.')

# usuario = int(input('Qual a sua idade: '))

# if usuario <= 12:
#     print('Você tem entre 0 a 12 anos')
# elif usuario <= 18:
#     print('Você tem entre 13 a 18 anos')
# else:
#     print('Você é maior de idade tem acima de 18')

# idade = int(input("Digite sua idade: "))
# if 0 < idade <= 12:
#     print("Criança")
# elif 12 < idade < 18:
#     print("Adolescente")
# elif idade >= 18:
#     print("Adulto")
# else: 
#     print("Valor inválido!")

# email = input('Digite seu e-mail: ')
# senha = int(input('Digite sua senha (apenas números): '))

# email_confirma = input('Confirme seu e-mail: ')
# senha_confirma = int(input('Confirme sua senha (apenas números): '))

# if email == email_confirma and senha == senha_confirma:
#     print('E-mail e senha confirmados com sucesso!')
# else:
#     print('E-mail ou senha não conferem.')

# usuario_correto = "alura"
# senha_correta = "alura123"

# usuario = input("Digite o nome de usuário: ")
# senha = input("Digite a senha: ")

# if usuario == usuario_correto and senha == senha_correta:
#     print("Login bem sucedido!")
# else:
#     print("Credenciais inválidas. Tente novamente.")

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")
