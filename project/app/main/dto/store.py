from flask_restplus import Namespace, fields

from .postal_code import PostalCode as PostalCodeDto


class Store:
    api = Namespace('store', description='store related operations')
    store = api.model('store', {
        'name': fields.String(required=True, description='store name'),
        'phone': fields.String(required=True, description='store phone'),
        'email': fields.String(required=True, description='store email'),
        'street': fields.String(required=True, description='street (address)'),
        'external_number': fields.String(
            required=True,
            description='external number (address)'),
        'internal_number': fields.String(
            description='Internal number (address)'),
        'postal_code_id': fields.Integer(
            required=True,
            description='zip code id (address)')
    })
    store_response = api.model('store_response', {
        'id': fields.Integer(attribute='id'),
        'name': fields.String(attribute='name'),
        'phone': fields.String(attribute='phone'),
        'email': fields.String(attribute='email'),
        'street': fields.String(attribute='street'),
        'external_number': fields.String(attribute='external_number'),
        'internal_number': fields.String(attribute='internal_number'),
        'postal_code': fields.Nested(PostalCodeDto.postal_code)
    })
    stock = api.model('stock', {
        'store_id': fields.Integer(
            required=True,
            description='store id'
        ),
        'product_id': fields.Integer(
            required=True,
            description='product id'
        ),
        'sku': fields.String(
            required=True,
            description='stored product sku'
        )
    })
