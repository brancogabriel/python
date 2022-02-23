from pessoa import Pessoa

pessoa1 = Pessoa('Gabriel', 25)
pessoa2 = Pessoa('Linda', 24)

pessoa1.comer('laranja')
pessoa1.falar('Bitcoin')
pessoa1.parar_comer()
pessoa1.falar('Bitcoin')
pessoa1.comer('laranja')
pessoa1.parar_falar()
pessoa1.parar_comer()
pessoa1.falar('Bitcoin')
pessoa2.falar('filmes')
pessoa2.parar_falar()
pessoa2.comer('sorvete')
print(pessoa1.get_ano_nascimento())