from flask import Flask, Blueprint
from flask_restful import Api
from resources.cliente import Clientes, Cliente

bp = Blueprint('app', __name__)

app = Flask(__name__)
api = Api(app)

api.add_resource(Clientes, '/clientes')
api.add_resource(Cliente, '/clientes/<int:cliente_id>')


if __name__ == '__main__':
    app.run(debug=True)
