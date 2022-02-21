variavel = 'valor'

def func():
    print(variavel)
    
def func2():
    variavel = 'Outro valor' #esta variável não é a mesma que a variável de cima, pois foi criada dentro da func2 e não está no escopo global
    print(variavel)
    
func()
func2()

print(variavel)
print('')


# para transformar a variavel da func2 no escopo global, é necessário fazer os ajuestes conforme abaixo

variavel2 = 'valor'

def func2():
    print(variavel2)
    
def func2():
    global variavel2
    variavel2 = 'Outro valor' 
    print(variavel2)
    
func()
func2()

print(variavel2)