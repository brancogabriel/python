""""
print('Gabriel', type('Gabriel'))
print(25, type(25))
print(1.60, type (1.60))
print(25>18, type(25>18))
"""
nome = 'Gabriel'
idade = 25
altura = 1.72
e_maior = idade > 18
peso = 76
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}') #.2f formata o numero de casas decimais
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu IMC é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é {ic:.2f}'.format(n=nome, i=idade, im=imc))

