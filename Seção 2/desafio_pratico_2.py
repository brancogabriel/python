'''
DESAFIO 1
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.


num = input('Digite um numero: ')

try:
    num = int(num)
    
    if num % 2 == 0:
        print('Número par.')
    else:
        print('Número ímpar.')
        
except: 
    print('Não é um número inteiro')
'''

'''DESAFIO 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Bom dia 0-11, Boa tarde 12-17, boa noite 18-23.

'''

hora = input('Informe o horário atual, sem considerar os minutos: ')

if hora.isdigit():
    hora = int(hora)
    
    if hora >= 0 and hora < 12:
        print('Bom dia')
    elif hora >= 12 and hora < 18:
        print('Boa tarde')
    elif hora >= 18 and hora < 0:
        print ('Boa noite')
    else:
        print('Digite um número entre 0 e 23')
else:
    print('Por favor, digite um número válido')


'''
DESAFIO 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".


nome = input('Informe o seu primeiro nome: ')

qtd_caracteres = len(nome)

if qtd_caracteres <= 4:
    print('Seu nome é muito curto')
elif qtd_caracteres > 4 and qtd_caracteres <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
'''