'''
* split - divide uma string
* join - junta strings
* enumerate - enumera itens de uma string
'''

'''
string = "O Brasil é o país do futebol. O Brasil é penta."
lista1 = string.split(' ')
lista2 = string.split('.')

print(lista1)
print(lista2)

for valor in lista1:
    print(valor)
    
for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase')
    
palavra = ''
contagem = 0

for valor in lista1:
    qtd_vezes = lista1.count(valor)
    
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
        
print(f'A palavra que apareceu mais vezes foi {palavra} ({contagem}x).')
'''

string = 'O Brasil é penta'
lista3 = string.split( )
string4 = ','.join(lista3)
print(string4)

for indice, valor in enumerate(lista3):
    print(indice,valor)
    
    