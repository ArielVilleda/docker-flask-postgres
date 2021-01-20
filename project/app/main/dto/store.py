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
    # Inherit fields from store
    store_response = api.inherit('store_response', store, {
        'id': fields.Integer(attribute='id'),
        'postal_code': fields.Nested(api.model('postal_code', {
                'id': fields.Integer(atribute='id'),
                'neighborhood': fields.String(atribute='neighborhood'),
                'district': fields.String(atribute='district'),
                'state': fields.String(atribute='state'),
                'city': fields.String(atribute='city'),
                'postal_code': fields.String(atribute='postal_code')
            }
        ))
    })
    stock = api.model('store_stock', {
        'product_id': fields.Integer(
            required=True,
            description='product id'
        ),
        'sku': fields.String(
            required=True,
            description='stored product sku'
        )
    })
    # Inherit fields from stock
    stock_response = api.inherit('store_stock_response', stock, {
        'id': fields.Integer(attribute='id'),
        'store_id': fields.Integer(attribute='store_id'),
        'product': fields.Nested(api.model('store_stock_product', {
                'id': fields.String(attribute='id'),
                'name': fields.String(attribute='name'),
                'image_url': fields.String(attribute='image_url')
            }
        ))
    })
