'''formatando valores com modificadores

:s - texto
:d - inteiros
:f - pontos flutuantes
:.(NÚMERO)f - quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - ESQUERDA
< - DIREITA
^ - CENTRO
'''

n1 = 10
n2 = 3
divisao = n1 / n2
print( '{:.2f}'.format(divisao) )
print( f'{divisao:.2f}' )

n3 = 1
print(f'{n3:0>10}') # adicionará 9 caracteres '0' à esquerda
print(f'{n3:0^10}') # adicionará 9 caracteres '0' ao redor do n3

nome = 'Homi'
sobrenome = 'Miranha'
print(f'{nome:#^50}') # adicionará  36 caracteres '#'ao redor do nome

nome_formatado1 = '{:@^20}'.format(nome) # 20 é a quantidade total de caracteres, somando os caracteres em 'nome'
nome_formatado2 = '{n:@^20}'.format(n=nome) # 20 é a quantidade total de caracteres, somando os caracteres em 'nome'
print(nome_formatado2)

nome_formatado3 = '{0:@^16} {1:#^16}'.format(nome, sobrenome)
print(nome_formatado3)
