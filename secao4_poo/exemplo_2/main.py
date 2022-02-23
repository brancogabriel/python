from random import randint

class Pessoa:
    ano_atual = 2022
    
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self): # self é a instancia, assim cada instancia terá seu ano de nascimento. Este é um método de instancia
        print(self.ano_atual - self.idade)
    
    @classmethod # metodo de classe
    def por_ano_nascimento(cls, nome, ano_nascimento): #cls é utilizado por convencao, mas pode ser qualquer texto
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod #metodo estatico
    def gera_id():
        rand = randint(10000, 99999)
        return rand
    
# p1 = Pessoa.por_ano_nascimento('Gabriel', 1996)
p1 = Pessoa ('Gabriel', 25)
print(p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id())
print(p1.gera_id())