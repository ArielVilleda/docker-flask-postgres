from flask_restplus import Namespace, fields


class Stock:
    api = Namespace('stock', description='stock related operations')
    stock = api.model('stock', {
        'store_id': fields.Integer(
            required=True,
            description='product id'
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
    # Inherit fields from stock
    stock_response = api.inherit('stock_response', stock, {
        'store': fields.Nested(api.model('stock_store', {
                'id': fields.Integer(attribute='id'),
                'name': fields.String(attribute='name'),
                'phone': fields.String(attribute='phone'),
                'email': fields.String(attribute='email'),
                'street': fields.String(attribute='street'),
                'external_number': fields.String(attribute='external_number'),
                'internal_number': fields.String(attribute='internal_number'),
                'postal_code_id': fields.Integer(attribute='postal_code_id'),
            }
        )),
        'product': fields.Nested(api.model('stock_product', {
                'id': fields.String(attribute='product_id'),
                'name': fields.String(attribute='product_name'),
                'image_url': fields.String(attribute='product_image_url')
            }
        ))
    })
