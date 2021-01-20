from flask_restplus import Namespace, fields


class Product:
    api = Namespace('product', description='product related operations')
    product = api.model('product', {
        'name': fields.String(required=True, description='product namep'),
        'image': fields.String(required=True,
                               description='product thumbnail  path')
    })
    product_response = api.model('product_response', {
        'id': fields.String(required=True, description='product identifier'),
        'name': fields.String(required=True, description='product namep'),
        'image': fields.String(required=True,
                               description='product thumbnail  path')
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
            description='stored product sku',
        )
    })
