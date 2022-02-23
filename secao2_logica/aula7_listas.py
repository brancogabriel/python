l1 = ['String', True, 10, -20.5]

for elem in l1:
    print(f'O tipo de {elem} é {type(elem)}')
    
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print( max(l2) ) # imprimi valor max
print( min(l2) ) # imprimi valor min

print()

l2.insert(0, 'banana') # insere banana na posição 0
print(l2)

print(l2[0:3]) # exibe a lista até o item 3
print(l2[::-1]) # exibe a lista de trás pra frente
print(l2[::2]) # exibe a lista de 2 em 2

l1.extend(l2) # adiciona os valos de l2 na l1
print(l1) 

l3 = list( range(0,100,7) )
print(l3)