# lista onde p = produto e o valor é o preço do produto
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]

def func(item): 
    return item[1]      # retorna todos os preços dos produtos

lista.sort(key=func)    # ordena a lista de forma crescente de acordo com o valor de func, ou seja, o preço
print(lista)

lista.sort(key=func, reverse=True)    # ordena a lista de forma decrescente de acordo com o valor de func, ou seja, o preço
print(lista)
print('')

# existe uma forma mais simples de ordenar a lista, utilizando funcoes anonimas:
lista.sort(key=lambda item: item[1], reverse=True) # lambda é a funcao anonima item que retorna o item[1]
print(lista)
print('')

# existe uma forma ainda mais simples de ordenar a lista, utilizando a funcao sorted

print(sorted(lista, key=lambda item: item[1]))