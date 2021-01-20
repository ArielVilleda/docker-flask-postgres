from flask import request
from flask_restplus import Resource

from app.main.models import Store as StoreModel
from app.main.models import Product as ProductModel
from app.main.models import Stock as StockModel
from app.main.dto import Store as StoreDto

store_api = StoreDto.api
_store = StoreDto.store
_store_response = StoreDto.store_response
_stock = StoreDto.stock
_stock_response = StoreDto.stock_response


@store_api.route('/')
class StoreList(Resource):
    @store_api.doc('list_of_registered_stores')
    @store_api.marshal_list_with(_store_response, envelope='data')
    def get(self):
        """List all registered stores with postal_code relation"""
        return StoreModel.with_postal_code().all()

    @store_api.response(201, 'Store successfully created.')
    @store_api.doc('create a new store')
    @store_api.expect(_store, validate=True)
    def post(self):
        """Creates a new Store"""
        data = request.json
        store = StoreModel.query.filter_by(email=data['email']).first()
        if store:
            response_object = {
                'status': 'fail',
                'message': 'Some data belongs to an existing Store',
            }
            return response_object, 409
        new_store = StoreModel(**data)
        new_store.save()
        response_object = {
            'status': 'success',
            'message': 'Store successfully created.',
            'store_id': new_store.id
        }
        return response_object, 201


@store_api.route('/<int:store_id>')
@store_api.param('store_id', 'The Store identifier')
@store_api.response(404, 'Store not found.')
class Store(Resource):
    @store_api.doc('get a store')
    @store_api.marshal_with(_store_response)
    def get(self, store_id):
        """Get a store given its identifier"""
        store = StoreModel.query.filter_by(id=store_id).first()
        if not store:
            store_api.abort(404, "Store {} doesn't exist".format(store_id))
        else:
            return store

    @store_api.doc('delete_store')
    @store_api.response(204, 'store deleted')
    def delete(self, store_id):
        """Delete a store given its identifier"""
        store = StoreModel.query.filter_by(id=store_id).first()
        if not store:
            store_api.abort(404, "Store {} not found".format(store_id))
        store.delete()
        return '', 204


@store_api.route('/<int:store_id>/stock')
@store_api.param('store_id', 'The Store identifier')
@store_api.response(404, 'Store or Product not found.')
class StoreStockList(Resource):
    @store_api.doc('list_of_registered_store_product')
    @store_api.marshal_list_with(_stock_response, envelope='data')
    def get(self, store_id):
        """List all products given the store relation"""
        store = StoreModel.query.filter_by(id=store_id).first()
        if not store or not store:
            store_api.abort(404, "Store {} doesn't exist".format(store_id))
        return store.products  # returns stock models

    @store_api.doc('add product to store')
    @store_api.expect(_stock)
    def post(self, store_id):
        """Associate product to the given store with the
        intermediate table 'stocks'
        """
        store = StoreModel.query.filter_by(id=store_id).first()
        if not store:
            store_api.abort(404, "Store {} not found".format(store_id))
        data = request.json
        product = ProductModel.query.filter_by(id=data['product_id']).first()
        if not product:
            store_api.abort(404,
                            "Product {} not found".format(data['product_id']))
        stock = StockModel.query.filter_by(sku=data['sku']).first()
        if stock:
            response_object = {
                'status': 'fail',
                'message': 'The sku was already assigned',
            }
            return response_object, 409
        stock = StockModel(sku=data['sku'])
        stock.product = product
        store.products.append(stock)
        store.save()
        response_object = {
            'status': 'success',
            'message': 'Stock successfully created.',
            'stock_id': stock.id,
        }
        return response_object, 201
