from flask import Flask, Blueprint
from flask_restful import Api
from resources.cliente import Clientes, Cliente
from resources.imovel import Imoveis, Imovel
from resources.contrato import Contratos, Contrato
from flask_swagger_ui import get_swaggerui_blueprint

bp = Blueprint('app', __name__)

app = Flask(__name__)
api = Api(app)

api.add_resource(Clientes, '/clientes')
api.add_resource(Cliente, '/clientes/<int:cliente_id>')

api.add_resource(Imoveis, '/imoveis')
api.add_resource(Imovel, '/imoveis/<int:imovel_id>')

api.add_resource(Contratos, '/contratos')
api.add_resource(Contrato, '/contratos/<int:id_contrato>')

SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  
    API_URL,
    config={  
        'app_name': "Api Imoveis"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
