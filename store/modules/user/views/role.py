from store.core.view import BaseView


class RoleView(BaseView):
    column_sortable_list = ('id', 'name',)
    column_editable_list = ('name',)
