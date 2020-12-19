from flask_restplus import Resource
from flask_cors import cross_origin

from .dto import UserDto
from .helper import register


api = UserDto.api


@api.route('/')
class HelloWorld(Resource):

    @cross_origin()
    @api.expect(UserDto.user_post)
    def post(self):
        return register()
