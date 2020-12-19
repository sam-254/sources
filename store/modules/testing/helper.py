from flask import request
import math


def article_by_pages(article):
    payload = request.json
    page = payload.get("page")
    items_per_page = payload.get('items_per_page')
    articles_end = items_per_page * page

    articles_start = items_per_page * page - items_per_page
    articles_to_show = article[articles_start: articles_end]

    total_pages = math.ceil(len(article) / items_per_page)

    response_object = {
        'status': 'success',
        'message': 'Articles responded successfully.',
        'data': {
            'page': page,
            'articles': articles_to_show,
            'itemsPerPage': items_per_page,
            'total_pages': total_pages
        }
    }

    return response_object, 200
