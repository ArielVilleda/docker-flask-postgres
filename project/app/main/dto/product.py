from flask_restplus import Namespace, fields

from .store import Store as StoreCodeDto


class Product:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'name': fields.String(required=True, description='product name'),
        'image_url': fields.String(required=True,
                                   description='product thumbnail url')
    })
    # Inherit fields from product
    product_response = api.inherit('product_response', product, {
        'id': fields.String(required=True, description='product identifier')
    })
