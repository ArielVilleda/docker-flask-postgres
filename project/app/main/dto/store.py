from flask_restplus import Namespace, fields


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
