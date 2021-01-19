from flask_restplus import Api
from flask import Blueprint

from .main.controllers.store import api as store_ns
from .main.controllers.postal_code import api as postal_code_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Cargamos\'s Technical Test',
    version='1.0',
    description='Store inventory services'
)

api.add_namespace(store_ns, path='/store')
api.add_namespace(postal_code_ns, path='/postal_code')
