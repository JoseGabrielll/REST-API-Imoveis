from flask_restful import Resource, reqparse
from models.cliente import ClienteModel

clientes = [
    {
        'cliente_id': 1,
        'nome': 'Carlos',
        'cpf': 112,
        'renda': 800.00
    },
    {
        'cliente_id': 2,
        'nome': 'Jose',
        'cpf': 102,
        'renda': 600.00
    },
    {
        'cliente_id': 3,
        'nome': 'Ana',
        'cpf': 992,
        'renda': 1100.00
    }
]

class Clientes(Resource):
    def get(self):
        return {'clientes': clientes}


class Cliente(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('cpf')
    argumentos.add_argument('renda')

    def find_cliente(cliente_id):
        for cliente in clientes:
            if cliente['cliente_id'] == cliente_id:
                return cliente
        return None
    
    def get(self, cliente_id):
        cliente = Cliente.find_cliente(cliente_id)

        if cliente is not None:
            return cliente
        return{'message':'Cliente não encontrado'}, 404
    
    def post(self, cliente_id):
       dados = Cliente.argumentos.parse_args()
       obj_cliente = ClienteModel(cliente_id, **dados)
       novo_cliente = obj_cliente.json()

       clientes.append(novo_cliente)
       return novo_cliente, 200 

    def put(self, cliente_id):
        pass

    def delete(self, cliente_id):
        pass
