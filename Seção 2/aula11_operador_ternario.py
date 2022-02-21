# logged_user = True
# msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar'
# print(msg)

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Usuário menor de idade'
    print(msg)