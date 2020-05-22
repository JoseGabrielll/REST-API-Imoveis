from flask_restful import Resource, reqparse
from models.contrato import ContratoModel
from db import get_db

class Contratos(Resource):
    def get(self):
        lista_contratos = []

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM contrato;")
        contratos = cursor.fetchall() 

        for contrato in contratos:
            id_contrato = contrato[0]
            id_cliente = contrato[1]
            id_imovel = contrato[2]

            contrato_atual = ContratoModel(id_contrato, id_cliente, id_imovel)
            lista_contratos.append(contrato_atual)
        
        return {'contratos': [contrato.json() for contrato in lista_contratos]}

class Contrato(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('id_cliente')
    argumentos.add_argument('id_imovel')

    def get(self, id_contrato): 

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM contrato WHERE id_contrato = %s;", (id_contrato,))
        contrato = cursor.fetchone()

        if contrato is not None:
            id_contrato = contrato[0]
            id_cliente = contrato[1]
            id_imovel = contrato[2]

            contrato_encontrado = ContratoModel(id_contrato, id_cliente, id_imovel)
            return contrato_encontrado.json()
        return{'message': 'Contrato não encontrado'}, 404


    def post(self, id_contrato):
        dados = Contrato.argumentos.parse_args()
        obj_contrato = ContratoModel(id_contrato, **dados)
        novo_contrato = obj_contrato.json()

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO contrato (id_cliente, id_imovel) \
                        VALUES (%s, %s)", \
                        (obj_contrato.id_cliente, obj_contrato.id_imovel))
        db.commit()

        return novo_contrato, 200

    def put(self, id_contrato):
        pass
    def delete(self, id_contrato):
        pass