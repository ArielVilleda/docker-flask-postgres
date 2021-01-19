from flask import request
from flask_restplus import Resource

from app.main.models import PostalCode as PostalCodeModel
from app.main.dto import PostalCode as PostalCodeDto

api = PostalCodeDto.api
_postal_code = PostalCodeDto.postal_code


@api.route('/')
class PostalCodeList(Resource):
    @api.doc('list_of_registered_postal_codes')
    @api.marshal_list_with(_postal_code, envelope='data')
    def get(self):
        """List all PostalCodes"""
        return PostalCodeModel.query.all()


@api.route('/<postal_code>')
@api.param('postal_code', 'The PostalCode identifier (5 digits)')
@api.response(404, 'PostalCode not found.')
class PostalCode(Resource):
    @api.doc('get PostalCode given 5 digit code')
    @api.marshal_with(_postal_code)
    def get(self, postal_code):
        """get PostalCode(s) given its identifier"""
        pcodes = PostalCodeModel.query.filter_by(
            postal_code=postal_code
        )
        print(postal_code)  # DEBUG
        result = pcodes.all()
        if not postal_code:
            api.abort(404)
        else:
            return result
