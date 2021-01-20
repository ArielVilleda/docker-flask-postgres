from flask_restplus import Api
from flask import Blueprint

from .main.controllers.postal_code import pcode_api as pcode_ns
from .main.controllers.store import store_api as store_ns
from .main.controllers.product import product_api as product_ns
from .main.controllers.stock import stock_api as stock_ns


blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Cargamos\'s Technical Test',
    version='1.0',
    description='Store inventory services'
)

api.add_namespace(pcode_ns, path='/postal_code')
api.add_namespace(product_ns, path='/product')
api.add_namespace(store_ns, path='/store')
api.add_namespace(stock_ns, path='/stock')
