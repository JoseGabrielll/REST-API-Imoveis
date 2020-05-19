from flask_restful import Resource, reqparse
from models.imovel import ImovelModel

class Imoveis(Resource):
    def get(self):
        return {'imoveis': imoveis}

class Imovel(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass