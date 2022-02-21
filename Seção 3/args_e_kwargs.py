# *args serve para não precisar explicitar individualmente os argumentos de uma função.
# ele não precisa se chamar *args, mas precisa, necessariamente, ter o *

def func(*args):
     print(args)

# exibe os valores da lista, sendo que n1 e n2 são desempacotados     
lista = [1,2,3,4,5]
n1, n2, *n = lista
print (n1, n2, n)

# a lista será desempacotada, por conta do uso do *
lista = [1,2,3,4,5]
print(*lista)

# a lista será desempacotada, por conta do uso do *, separada por -
lista = [1,2,3,4,5]
print(*lista, sep='-')