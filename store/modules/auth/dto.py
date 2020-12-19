from flask_restplus import Namespace, fields


class AuthDto:
    api = Namespace('auth', description='Auth namespace')

    auth_post = api.model('auth_post', {
        'email': fields.String(description='User email', required=True),
        'password': fields.String(description='User password', requred=True),
    })
