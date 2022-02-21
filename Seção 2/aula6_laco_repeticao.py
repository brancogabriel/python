while True:
    print()
    sair = input('Deseja sair? [s]im ou [n]ão: ')
    
    if sair == 's':
        break
    
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    oper = input('Digite um operador: ')
        
    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número.')
        continue
        
    num1 = int(num1)
    num2 = int(num2)

    if oper == '+':
        print(f'A soma dos números é {num1 + num2}')
    elif oper =='-':
        print(f'A subtração dos números é {num1 - num2}')
    elif oper =='*':
        print(f'A multiplicação dos números é {num1 * num2}')
    elif oper =='/':
        print(f'A divisão dos números é {num1 / num2}')