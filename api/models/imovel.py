class ImovelModel:
    def __init__(self, imovel_id, situacao, valor):
        self.imovel_id = imovel_id
        self.situacao = situacao
        self.valor = valor

    def json(self):
        return {
            'imovel_id': self.imovel_id,
            'situacao': self.situacao,
            'valor': self.valor
        }
        
    #def find_imovel()
'''
ImovelModel.situacao:
-1: livre / disponivel
-2: alugado
-3: vendido
'''
