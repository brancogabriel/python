while True:
    cpf = input('Digite um cpf: ')
    novo_cpf = cpf[:-2]
    reverso = 10
    soma = 0

    for index in range(19): 
        if index > 8:
            index -= 9 # verifica até o nono número da string, zera e verifica até o décimo número da string

        soma += int(novo_cpf[index]) * reverso # reverso é o número cujo valor do índice é multiplicado
        
        reverso -= 1 
        if reverso < 2:
            reverso = 11
            d = 11 - (soma % 11)
            
            if d > 9:
                d = 0
            soma = 0
            novo_cpf += str(d)

    if cpf == novo_cpf:
        print('Válido')
    else:
        print ('Inválido')