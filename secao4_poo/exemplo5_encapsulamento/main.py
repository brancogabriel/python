"""
Convencao Python para setar atributos:
_ -> privado/protected (public _)
__ -> privado (_NOMECLASSE__nomeatributo
"""

class BaseDeDados: # cria a classe
    def __init__(self): # construtor da classe (primeira funcao da classe)
        self.dados = {} # cria o dicionario - coracao da classe

    def inserir_moradores(self, id, nome): # funcao para inserir moradores dentro do array
        if 'moradores' not in self.dados: # verifica se o morador não existe no array
            self.dados['moradores'] = {id: nome} # cadastra o morador dentro do array
        else:
            self.dados['moradores'].update({id: nome}) # atualiza o nome do morador referente ao id já existente
    
    def lista_moradores(self): # funcao para listar todos os moradores dentro do array
        for id, nome in self.dados['moradores'].items():
            print(id, nome)
    
    def apaga_morador(self, id): # funcao para apagar um morador do array, de acordo com o id
        del self.dados['moradores'][id]
        
bd = BaseDeDados()
bd.inserir_moradores(1, 'Gabriel')
bd.inserir_moradores(2, 'Linda')
bd.inserir_moradores(3, 'Érico')
bd.lista_moradores()