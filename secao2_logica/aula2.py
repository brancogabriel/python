# nome = input('Qual é o seu nome? ')
# idade = input('Qual é a sua idade? ')

# ano_nascimento = 2021 - int(idade)

# print()
# print (f'{nome} tem {idade} anos. ' 
#        f'{nome} nasceu em {ano_nascimento}.')

# -------------------------------------------------

# print('Essa é uma calculadora simples de soma.')

# print()

# numero_1 = int(input('Digite um número: '))
# numero_2 = int(input('Digite outro número: '))

# resultado = numero_1 + numero_2

# print(f'A soma dos dois números é {resultado}')

# -------------------------------------------------

nome = input('Qual é o seu nome? ')
idade = input ('Qual é a sua idade? ')

idade = int(idade)
qtd_caracteres = len(nome) 

print()

print(f'Este nome possui {qtd_caracteres} caracteres.')

if idade < 18 and idade > 30:
    print(f'{nome} não pode pegar o empréstimo')
else:
    print(f'{nome} pode pegar o empréstimo')