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


@store_api.route('/')
class StoreList(Resource):
    @store_api.doc('list_of_registered_stores')
    @store_api.marshal_list_with(_store_response, envelope='data')
    def get(self):
        """List all registered stores with postal_code relation"""
        return StoreModel.all()

    @store_api.response(201, 'Store successfully created.')
    @store_api.doc('create a new store')
    @store_api.expect(_store, validate=True)
    def post(self):
        """Creates a new Store """
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
        """get a store given its identifier"""
        store = StoreModel.query.filter_by(id=store_id).first()
        if not store:
            store_api.abort(404)
        else:
            return store
