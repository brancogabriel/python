from pessoa import Pessoa
"""
p1 = Pessoa() # estamos criando um objeto (p1) à partir de uma classe. 
p2 = Pessoa() # p1 é diferente de p2, conforme exibido no print abaixo. Estão alocadas em espaços diferentes da memória

print(p1)
print(p2)

p1.falar() # só funcionou assim pois foi informado que a instancia vai dentro da funcao no arquivo pessoa.py (utilizando o self, verificar no outro arquivo). Se nao, seria necessário informar p1.falar(p1)

"""

p1 = Pessoa('Gabriel', 25)
p1.comer('maçã')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('alimento')
p1.parar_falar()
p1.falar('assunto')

