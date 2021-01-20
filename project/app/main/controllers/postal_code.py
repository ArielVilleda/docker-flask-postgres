from flask import request
from flask_restplus import Resource

from app.main.models import PostalCode as PostalCodeModel
from app.main.dto import PostalCode as PostalCodeDto

pcode_api = PostalCodeDto.api
_pcode = PostalCodeDto.postal_code


@pcode_api.route('/')
class PostalCodeList(Resource):
    @pcode_api.doc('list_of_registered_postal_codes')
    @pcode_api.marshal_list_with(_pcode, envelope='data')
    def get(self):
        """List all PostalCodes"""
        return PostalCodeModel.query.all()


@pcode_api.route('/<postal_code>')
@pcode_api.param('postal_code', 'The PostalCode identifier (5 digits)')
@pcode_api.response(404, 'PostalCode not found.')
class PostalCode(Resource):
    @pcode_api.doc('get PostalCode given 5 digit code')
    @pcode_api.marshal_with(_pcode)  # match with this model for response
    def get(self, postal_code):
        """get PostalCode(s) given its identifier"""
        pcodes = PostalCodeModel.query.filter_by(
            postal_code=postal_code
        )
        result = pcodes.all()
        if not postal_code:
            pcode_api.abort(404)
        else:
            return result
