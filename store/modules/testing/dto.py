from flask_restplus import Namespace, fields


class TestingDto:
    api = Namespace('testing', description='Testing namespace')

    article_post = api.model('article_post', {
        'page': fields.Integer(description='article page', required=True),
        'items_per_page': fields.Integer(description='article items_per_page', required=True),
    })
