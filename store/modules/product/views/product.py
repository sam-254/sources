from store.core.view import BaseView


class ProductView(BaseView):
    column_list = ('id', 'sku', 'title', 'created_at', 'updated_at',)
