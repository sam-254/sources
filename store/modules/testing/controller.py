from flask_restplus import Resource
from flask_cors import cross_origin
from flask import jsonify

from .helper import article_by_pages

from .dto import TestingDto

api = TestingDto.api

students = [
    {'name': 'Mark', 'age': 23, 'spec': 'math'},
    {'name': 'Jane', 'age': 20, 'spec': 'biology'},
    {'name': 'Peter', 'age': 21, 'spec': 'history'},
    {'name': 'Kate', 'age': 22, 'spec': 'science'},
]

articles = [
    {
        'text': 'article_1',
    },
    {
        'text': 'article_2',
    },
    {
        'text': 'article_3',
    },
    {
        'text': 'article_4',
    },
    {
        'text': 'article_5',
    },
    {
        'text': 'article_6',
    },
    {
        'text': 'article_7',
    },
    {
        'text': 'article_8',
    },
    {
        'text': 'article_9',
    },
    {
        'text': 'article_10',
    },
    {
        'text': 'article_11',
    },
    {
        'text': 'article_12',
    },
    {
        'text': 'article_13',
    },
  {
        'text': 'article_14',
    },
  {
        'text': 'article_15',
    },
]


@api.route('/')
class Testing(Resource):
    """Product Resource"""

    @cross_origin()
    def get(self):
        """list"""

        return jsonify(students)


@api.route('/article/')
class Article(Resource):
    """Product Resource"""

    @cross_origin()
    def get(self):
        """list"""

        return jsonify(articles)

    @api.expect(TestingDto.article_post)
    @cross_origin()
    def post(self):
        """Articles by page"""

        return article_by_pages(articles)
