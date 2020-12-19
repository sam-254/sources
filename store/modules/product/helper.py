from store.modules.product.models.product import Product
from flask import request
import jsonify
import json
import pprint
from flask_restplus import abort


def title_to_handle(title):
    return title


def create_product():
    payload = request.json

    sku = payload.get("sku")
    title = payload.get('title')
    namespace = payload.get('namespace')
    total_inventory = payload.get('total_inventory')

    product = Product.get_by_sku(sku)
    if product:
        abort(400, 'Product already exists.', status='fail')

    product = Product()
    product.sku = sku
    product.title = title
    product.namespace = namespace
    product.total_inventory = total_inventory

    product.save()

    response_object = {
        'status': 'success',
        'message': 'Product created successfully.'
    }

    return response_object, 201


def get_all_products():
    product = Product()
    product_list = product.get_all()

    products = []
    for product in product_list:
        products.append(
            {
                'id': product.id,
                'title': product.title,
                'product_type': product.product_type,
                'taxable': product.taxable,
                'sku': product.sku,

            }
        )
    response_object = {
        'status': 'success',
        'message': 'Product created successfully.',

        'data': products,

    }
    print(response_object)
    return response_object, 201


def delete_product():
    payload = request.json
    id = payload.get("id")

    product = Product()
    current_product = product.get_by_id(id)

    if not current_product:
        abort(400, 'Product does not exist.', status='fail')

    current_product.remove()

    response_object = {
        'status': 'success',
        'message': 'Product removed successfully.',
    }

    return response_object
