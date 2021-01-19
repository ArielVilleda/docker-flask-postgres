from flask_restplus import Resource, fields

ns = api.namespace('stores', description='Store Rest services')

store = api.model('Store', {
    'id': fields.Integer(readonly=True, description='Store unique identifier'),
    'name': fields.String(required=True, description='The store name')
})


# class StoreDAO(object):
#     def __init__(self):
#         self.counter = 0
#         self.stores = []

#     def get(self, id):
#         for todo in self.todos:
#             if todo['id'] == id:
#                 return todo
#         api.abort(404, "Todo {} doesn't exist".format(id))

#     def create(self, data):
#         todo = data
#         todo['id'] = self.counter = self.counter + 1
#         self.todos.append(todo)
#         return todo

#     def update(self, id, data):
#         todo = self.get(id)
#         todo.update(data)
#         return todo

#     def delete(self, id):
#         todo = self.get(id)
#         self.todos.remove(todo)


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all stores, and lets you POST to add new tasks'''
    @ns.doc('list_stores')
    @ns.marshal_list_with(store)
    def get(self):
        '''List all tasks'''
        return DAO.stores

    @ns.doc('create_store')
    @ns.expect(store)
    @ns.marshal_with(store, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'store not found')
@ns.param('id', 'The task identifier')
class Store(Resource):
    '''Show a single store item and lets you delete them'''
    @ns.doc('get_store')
    @ns.marshal_with(store)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_store')
    @ns.response(204, 'store deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(store)
    @ns.marshal_with(store)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)
