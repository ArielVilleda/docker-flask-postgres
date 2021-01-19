from flask import request
from flask_restplus import Resource

from app.main.models import Store as StoreModel
from app.main.dto import Store as StoreDto

api = StoreDto.api
_store = StoreDto.store


@api.route('/')
class StoreList(Resource):
    @api.doc('list_of_registered_stores')
    @api.marshal_list_with(_store, envelope='data')
    def get(self):
        """List all registered stores"""
        return StoreModel.query.all()

    @api.response(201, 'Store successfully created.')
    @api.doc('create a new store')
    @api.expect(_store, validate=True)
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
            'store': new_store
        }
        return response_object, 201


@api.route('/<id>')
@api.param('id', 'The Store identifier')
@api.response(404, 'Store not found.')
class Store(Resource):
    @api.doc('get a store')
    @api.marshal_with(_store)
    def get(self, id):
        """get a store given its identifier"""
        store = StoreModel.query.filter_by(id=id).first()
        if not store:
            api.abort(404)
        else:
            return store
