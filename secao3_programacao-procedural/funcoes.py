def divisao (n1, n2):
    if n2 > 0:
        return n1 / n2
    
divide = divisao(8, 0)

if divide:
    print(divide)
else: # divide = none
    print('Conta inválida')