# 1. Crie uma função que exiba uma saudação com os parâmetros saudação e nome

def msg(saudacao, nome):
    print(f'{saudacao} {nome}') 
    
msg('Seja bem vindo', 'Gabriel')

# 2. Cria uma função que receba três números como parâmetros e exiba a soma entre eles

def sum(n1, n2, n3):
    print(n1 + n2 + n3)

sum(1 ,2 ,3)


# 3. Crie uma função que recebe dois números, o primeiro é um valor e o segundo, um percentual. Retorne o valor do primeiro número somado do aumento percentual do mesmo

def recebe(n4, n5):
    print (n4 + (n5/100)*n4)
    
recebe (10, 10)

# 4. Fizz Buzz. Se o parâmetro da função for divisível por 3, retorne fizz, se for divisível por 5, retorne buzz. Se for divisível por 5 e por 3, retorne FizzBuzz. Caso contrário, retorne o número enviado

def funcao(n6):
    if n6 % 3 == 0 and n6 % 5 != 0:
        return ('Fizz')
    elif n6 % 3 != 0 and n6 % 5 == 0:
        return ('Buzz')
    elif n6 % 3 == 0 and  n6 % 5 == 0:
        return ('BuzzFizz')
    return n6
    
from random import randint

for i in range(10):
    aleatorio = randint (0, 100)
    print(funcao(aleatorio))            
