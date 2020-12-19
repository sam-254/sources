from flask import request
from flask_restplus import Resource
from flask_cors import cross_origin

from .dto import AuthDto
from .helper import AuthHelper
from store.core.helper import token_required

api = AuthDto.api

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """

    @api.doc('user login')
    @api.expect(AuthDto.auth_post, validate=True)
    @cross_origin()
    def post(self):
        """Post"""
        # post_data = request.json
        return AuthHelper.login_user()

    @token_required
    def get(self):
        """Get"""
        return AuthHelper.get_logged_in_user(), 200
