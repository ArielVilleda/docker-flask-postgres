from flask import request
from flask_restplus import Resource

from app.main.models import Stock as StockModel
from app.main.dto import Stock as StockDto

stock_api = StockDto.api
_stock = StockDto.stock
_stock_response = StockDto.stock_response


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
            stock_api.abort(404, "Stock {} doesn't exist".format(stock_id))
        else:
            return stock

    @stock_api.doc('delete_stock')
    @stock_api.response(204, 'stock deleted')
    def delete(self, id):
        """Delete a stock given its identifier"""
        StockModel.delete(id)
        return '', 204

    @stock_api.expect(_stock)
    @stock_api.marshal_with(_stock_response)
    def put(self, id):
        """Update a stock given its identifier"""
        return StockModel.update(id, stock_api.payload)
