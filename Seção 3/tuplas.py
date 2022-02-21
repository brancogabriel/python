# tuplas sao como listas, porém não é possível editar os valores dentro da lista. Não é possível alterar, remover ou adicionar novos valores

t1 = (1,2,3, 'a', 'Gabriel Branco') # a diferenca entre tupla e lista é que a tupla fica entre parenteses ou sem nada, enquanto a lista fica entre chaves

print(t1)

t2 = 1 # declarando um int
t3 = 1, # declarando uma tupla com um elemento
t4 = 1,2,3,4 # declarando uma tupla com vários elementos

# para editar uma lista, é possível gerar uma lista de uma tupla

t5 = (1, 2, 3, 4, 5)
t5 = list(t5)
t5[1] = 700

print(t5)

t5 = tuple(t5)
print(t5)