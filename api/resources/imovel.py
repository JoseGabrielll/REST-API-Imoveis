from flask_restful import Resource, reqparse
from models.imovel import ImovelModel
from db import get_db

class Imoveis(Resource):
    def get(self):
        lista_imoveis = []

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM imovel;")
        imoveis = cursor.fetchall()

        for imovel in imoveis:
            imovel_id = imovel[0]
            situacao = imovel[1]
            valor = imovel[2]

            imovel_atual = ImovelModel(imovel_id, situacao, valor)
            lista_imoveis.append(imovel_atual)
        
        return {'imoveis': [imovel.json() for imovel in lista_imoveis]}
            

class Imovel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('situacao')
    argumentos.add_argument('valor')

    def get(self, imovel_id):
        
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM imovel WHERE id_imovel = %s;", (imovel_id,))
        imovel = cursor.fetchone()

        if imovel is not None:
            situacao = imovel[1]
            valor = imovel[2]

            imovel_encontrado = ImovelModel(imovel_id, situacao, valor)
            return imovel_encontrado.json()
        
        return{'message': 'Imovel não encontrado'}, 404

    def post(self, imovel_id):
        dados = Imovel.argumentos.parse_args()
        obj_imovel = ImovelModel(imovel_id, **dados)
        novo_imovel = obj_imovel.json()

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO imovel (situacao, valor) \
                        VALUES (%s,%s)", \
                        (obj_imovel.situacao, obj_imovel.valor))
        db.commit()
        
        return novo_imovel, 200

    def put(self):
        pass

    def delete(self):
        pass