from flask_admin.contrib.sqla import ModelView


class BaseView(ModelView):
    column_display_pk = True
