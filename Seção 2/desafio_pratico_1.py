"""
Criar variáveis para nome(str) , idade(int), altura(float) e peso (float) de uma pessoa
Criar variável com o ano atual (int)
Obter o ano de nascimento de uma pessoa (baseado na idade e no ano atual)
Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa)
Exibir um texto com todos os valores da tela usando F-strings (com as chaves)

Exemplo da frase: 
Gabriel tem 25 anos, 1.72 de altura e pesa 76kg.
O IMC de Gabriel é 123.45.
Gabriel nasceu em 1996
"""


nome = 'Gabriel'
idade = 25
ano_atual = 2021
nascimento = ano_atual - idade
altura = 1.72
peso = 76.0
imc = peso / (altura ** 2)

print('{} tem {} anos de idade, {} de altura e pesa {}.'.format(nome, idade, altura, peso))
print('O IMC de {} é {:.2f}.'.format(nome, imc))
print('{} nasceu em {}.'.format(nome, ano_atual))


