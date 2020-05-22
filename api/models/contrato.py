class ContratoModel:
    def __init__(self, id_contrato, id_cliente, id_imovel):
        self.id_contrato = id_contrato
        self.id_cliente = id_cliente
        self.id_imovel = id_imovel
    
    def json(self):
        return {
            'id_contrato': self.id_contrato,
            'id_cliente': self.id_cliente,
            'id_imovel': self.id_imovel
        }
    
    #def find_contrato()