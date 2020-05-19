class ContratoModel:
    def __init__(self, contrato_id, cliente_id, imovel_id):
        self.contrato_id = contrato_id
        self.cliente_id = cliente_id
        self.imovel_id = imovel_id
    
    def json(self):
        return {
            'contrato_id': self.contrato_id,
            'cliente_id': self.cliente_id,
            'imovel_id': self.imovel_id
        }
    
    #def find_contrato()