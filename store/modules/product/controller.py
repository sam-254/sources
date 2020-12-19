from flask import request
import jsonify
from flask_restplus import Resource
from flask_cors import cross_origin

from store.core.helper import token_required
from .helper import *
from .dto import ProductDto

api = ProductDto.api


@api.route('/')
class Product(Resource):
    """Product Resource"""

    def get(self):
        """list"""

        return get_all_products(), 201

    @cross_origin()
    @api.expect(ProductDto.product_post)
    def post(self):
        """Create product"""

        return create_product()

    @cross_origin()
    @api.expect(ProductDto.product_delete)
    def delete(self):
        """Delete Product"""

        return delete_product()
