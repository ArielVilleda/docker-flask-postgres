from flask import request
from flask_restplus import Resource

from app.main.models import Stock as StockModel
from app.main.models import Product as ProductModel
from app.main.models import Store as StoreModel
from app.main.dto import Stock as StockDto

stock_api = StockDto.api
_stock = StockDto.stock
_stock_response = StockDto.stock_response
_stock_stats = StockDto.stock_stats


@stock_api.route('/<int:stock_id>')
@stock_api.param('stock_id', 'The Stock identifier')
@stock_api.response(404, 'Stock not found.')
class Stock(Resource):
    @stock_api.doc('get a stock')
    @stock_api.marshal_with(_stock_response)
    def get(self, stock_id):
        """Get a stock given its identifier"""
        stock = StockModel.query.filter_by(id=stock_id).first()
        if not stock:
            stock_api.abort(404, "Stock {} not found".format(stock_id))
        else:
            return stock

    @stock_api.doc('delete_stock')
    @stock_api.response(204, 'stock deleted')
    def delete(self, stock_id):
        """Delete a stock given its identifier"""
        stock = StockModel.query.filter_by(id=stock_id).first()
        if not stock:
            stock_api.abort(404, "Stock {} not found".format(stock_id))
        stock.delete()
        return '', 204

    @stock_api.expect(_stock)
    @stock_api.marshal_with(_stock_response)
    def put(self, stock_id):
        """Update a stock given its identifier"""
        stock = StockModel.query.filter_by(id=stock_id).first()
        if not stock:
            stock_api.abort(404, "Stock {} not found".format(stock_id))
        data = request.json
        store = StoreModel.query.filter_by(id=data['store_id']).first()
        if not store:
            stock_api.abort(404, "Store {} not found".format(data['store_id']))
        product = ProductModel.query.filter_by(id=data['product_id']).first()
        if not product:
            stock_api.abort(404,
                            "Product {} not found".format(data['product_id']))
        if StockModel.query.filter_by(sku=data['sku']).first():
            response_object = {
                'status': 'fail',
                'message': 'The sku was already assigned',
            }
            return response_object, 409
        stock.product = product
        stock.sku = data['sku']
        store.products.append(stock)
        store.save()
        return stock


@stock_api.route('/stats')
@stock_api.response(422, 'Incorrect params.')
@stock_api.response(200, 'Stats')
class StockStats(Resource):
    @stock_api.expect(_stock_stats)
    @stock_api.doc("querys for stocks' stats")
    def post(self):
        """Querys for stock table"""
        data = request.json
        if 'store_id' not in data:
            response_object = {
                'status': 'fail',
                'message': 'The store_id is required',
            }
            return response_object, 422
        parsed_data = {'store_id': data['store_id']}
        if 'product_id' in data:
            parsed_data['product_id'] = data['product_id']
        stock = StockModel.query.filter_by(**parsed_data).count()
        response_object = {
            'availability': stock,
        }
        return response_object, 200
