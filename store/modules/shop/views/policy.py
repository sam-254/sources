from store.core.view import BaseView


class PolicyView(BaseView):
    column_list = ('id', "title",)


class PrivacyView(BaseView):
    column_list = ('id', "title", 'shop')


class RefundView(BaseView):
    column_list = ('id', "title", 'shop')


class ServiceView(BaseView):
    column_list = ('id', "title", 'shop')
