from flask_restplus import Namespace, fields


class ProductDto:
    api = Namespace('product', description='Product namespace')

    product_post = api.model('product_post', {
        'sku': fields.String(description='Product sku', required=True),
        'title': fields.String(description='Product title', required=True),
        'namespace': fields.String(description='Product namespace', required=True),
        'total_inventory': fields.Integer(description='Product total inventory', required=True),
    })

    product_delete = api.model('product_delete', {
        'id': fields.Integer(description='Product id', required=True),
    })
