from flask_restplus import Namespace, fields


class PostalCode:
    api = Namespace('postal_code', description='postal_code related operations')
    postal_code = api.model('postal_code', {
        'id': fields.Integer(
            required=True,
            description='Integer identificator'),
        'neighborhood': fields.String(required=True, description='neighborhood'),
        'district': fields.String(required=True, description='district'),
        'state': fields.String(required=True, description='state'),
        'city': fields.String(required=True, description='city'),
        'postal_code': fields.String(required=True, description='zip code')
    })
