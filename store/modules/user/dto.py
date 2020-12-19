from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='User namespace')

    user_post = api.model('user_post', {
        'name': fields.String(description='User name'),
        'email': fields.String(description='User email', required=True),
        'password': fields.String(description='User password', requred=True),
        'age': fields.Integer(description='User age'),
    })
