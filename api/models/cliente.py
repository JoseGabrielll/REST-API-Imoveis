class ClienteModel:
    def __init__(self, cliente_id, nome, cpf, renda):
        self.cliente_id = cliente_id
        self.nome = nome
        self.cpf = cpf
        self.renda = renda
    
    def json(self):
        return {
            'cliente_id': self.cliente_id,
            'nome': self.nome,
            'cpf': self.cpf,
            'renda': self.renda
        }
