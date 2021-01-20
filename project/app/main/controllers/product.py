from flask import request
from flask_restplus import Resource

from app.main.models import Product as ProductModel
# from app.main.models import Stock as StockModel
from app.main.dto import Product as ProductDto

product_api = ProductDto.api
_product = ProductDto.product
_product_response = ProductDto.product_response


@product_api.route('/')
class ProductList(Resource):
    @product_api.doc('list_of_registered_products')
    @product_api.marshal_list_with(_product_response, envelope='data')
    def get(self):
        """List all registered products with postal_code relation"""
        return ProductModel.query.all()

    @product_api.response(201, 'Product successfully created.')
    @product_api.doc('create a new product')
    @product_api.expect(_product, validate=True)
    def post(self):
        """Creates a new Product """
        data = request.json
        new_product = ProductModel(**data)
        new_product.save()
        response_object = {
            'status': 'success',
            'message': 'Product successfully created.',
            'product_id': new_product.id
        }
        return response_object, 201


@product_api.route('/<int:product_id>')
@product_api.param('product_id', 'The Product identifier')
@product_api.response(404, 'Product not found.')
class Product(Resource):
    @product_api.doc('get a product')
    @product_api.marshal_with(_product_response)
    def get(self, product_id):
        """Get a product given its identifier"""
        product = ProductModel.query.filter_by(id=product_id).first()
        if not product:
            product_api.abort(404, "Product {} not found".format(product_id))
        else:
            return product

    @product_api.doc('delete_product')
    @product_api.response(204, 'product deleted')
    def delete(self, product_id):
        """Delete a product given its identifier"""
        product = ProductModel.query.filter_by(id=product_id).first()
        if not product:
            product_api.abort(404, "Product {} not found".format(product_id))
        product.delete()
        return '', 204
