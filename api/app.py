from flask import Flask, Blueprint
from flask_restful import Api
from resources.cliente import Clientes, Cliente
from resources.imovel import Imoveis, Imovel
from resources.contrato import Contratos, Contrato

#bp = Blueprint('app', __name__)

app = Flask(__name__)
api = Api(app)

api.add_resource(Clientes, '/clientes')
api.add_resource(Cliente, '/clientes/<int:cliente_id>')

api.add_resource(Imoveis, '/imoveis')
api.add_resource(Imovel, '/imoveis/<int:imovel_id>')

api.add_resource(Contratos, '/contratos')
api.add_resource(Contrato, '/contratos/<int:id_contrato>')


if __name__ == '__main__':
    app.run(debug=True)
