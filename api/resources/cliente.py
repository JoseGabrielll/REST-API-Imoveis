from flask_restful import Resource, reqparse
from models.cliente import ClienteModel
from db import get_db

class Clientes(Resource):
    def get(self):
        lista_clientes = []
    
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cliente;")
        clientes = cursor.fetchall()       

        for cliente in clientes:
            cliente_id = cliente[0]
            nome = cliente[1]
            cpf = cliente[2]
            renda = cliente[3]

            cliente_atual = ClienteModel(cliente_id, nome, cpf, renda)
            lista_clientes.append(cliente_atual)
        
        return {'clientes': [cliente.json() for cliente in lista_clientes]}


class Cliente(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('cpf')
    argumentos.add_argument('renda')
     
    def get(self, cliente_id):
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cliente WHERE id_cliente = %s;", (cliente_id,))
        cliente = cursor.fetchone()

        if cliente is not None:
            nome = cliente[1]
            cpf = cliente[2]
            renda = cliente[3]

            cliente_encontrado = ClienteModel(cliente_id, nome, cpf, renda)
            return cliente_encontrado.json()
        return{'message':'Cliente não encontrado'}, 404
    
    def post(self, cliente_id):
        dados = Cliente.argumentos.parse_args()
        obj_cliente = ClienteModel(cliente_id, **dados)
        novo_cliente = obj_cliente.json()
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO cliente (nome, cpf, renda) \
                        VALUES (%s,%s,%s)", \
                        (obj_cliente.nome, obj_cliente.cpf, obj_cliente.renda))
        db.commit()

        return novo_cliente, 200 

    def put(self, cliente_id):
        pass

    def delete(self, cliente_id):
        pass
