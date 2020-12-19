from store.modules.user.models.user import User

from flask import request


class AuthHelper:
    @staticmethod
    def login_user():
        data = request.json
        email = data.get('email')
        password = data.get('password')
        # ip = request.remote_addr
        # db.session.add(ip)
        user = User.query.filter_by(email=email).first()

        if not user and not user.check_password(password):
            response_object = {
                'status': 'fail',
                'message': 'email or password does not match.'
            }
            return response_object, 401
        else:
            auth_token = user.encode_auth_token(user.id)
            if auth_token:
                response_object = {
                    'status ': 'success',
                    'message': 'Successfully logged in.',

                    'id': user.id,
                    'email': user.email,
                    'Authorization': auth_token.decode()

                }
                return response_object, 200


    @staticmethod
    def get_logged_in_user():
        auth_token = request.headers.get('Authorization')
        if not auth_token:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

        response = User.decode_auth_token(auth_token)
        print('response ______________________________________________', response)
        if not isinstance(response, int):
            response_object = {
                'status': 'fail',
                'message': response
            }
            return response_object, 400

        user = User.get_by_id(response)
        if not user:
            response_object = {
                'status': 'fail',
                'message': response
            }
            return response_object, 401

        response_object = {
            'status': 'success',
            'message': 'Successfully logged in.',
            'data': {
                'id': user.id,
                'email': user.email,
                'Authorization': auth_token
            }
        }
        return response_object, 200
