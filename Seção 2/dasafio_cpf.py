'''
CPF = 168.995.350-09

1 * 10 = 10                 1 * 11 = 11
6 * 9 = 54                  6 * 10 = 60
8 * 8 = 64                  8 * 9 = 72
9 * 7 = 63                  9 * 8 = 72 
9 * 6 = 54                  9 * 7 = 63
5 * 5 = 25                  5 * 6 = 30
3 * 4 = 12                  3 * 5 = 15
5 * 3 = 15                  5 * 4 = 20
0 * 2 = 0                   0 * 3 = 0
                            0 * 2 = 0
        297                         343
11 - (297 % 11) = 11        11 - (343 % 11) = 9
11 > 9 = 0                                  
Dígito 1 = 0                Dígito 2 = 9
'''                     

cpf = input('Digite um número de CPF no formato XXX.XXX.XXX-XX: ')
i = 0
operador_multiplicacao = 0
operador_soma1 = 0
operador_soma2 = 0
contador_regressivo1 = 10
contador_regressivo2 = 11
digito1 = 0
digito2 = 0
calculo1 = 0
calculo2 = 0
novocpf = 0

while True: 
    if not len(cpf) == 14:
        print('Número inválido. Digite novamente: ')
        continue
    
    # realiza a soma da multiplicação de todos os dígitos da parte 1
    for i in cpf:
        if i < 12:
            if cpf[i] == ('.') or cpf[i] == ('-'):
                i += 1
            else:
                operador_multiplicacao = cpf[i] * contador_regressivo1
                operador_soma1 += operador_multiplicacao
                operador_multiplicacao = 0
                contador_regressivo1 -= 1
                i += 1
        else:
            i = 0
            break
    
    # identifica o digito 1
    calculo1 = 11 - (operador_soma1 % 11 ) 
    if calculo1 > 9:
        digito1 = 0
    else:
        digito1 = calculo1
        
    # realiza a soma da multiplicação de todos os dígitos da parte 1
    for i in cpf:
        if i < 14:
            if cpf[i] == ('.') or cpf[i] == ('-'):
                i += 1
            else:
                operador_multiplicacao = cpf[i] * contador_regressivo2
                operador_soma2 += operador_multiplicacao
                operador_multiplicacao = 0
                contador_regressivo2 -= 1
                i += 1
        else:
            i = 0
            break
    
    # identifica o digito 2
    calculo2 = 11 - (operador_soma2 % 11 ) 
    if calculo2 > 9:
        digito2 = 0
    else:
        digito2 = calculo2

    print (digito1, '-', digito2)

