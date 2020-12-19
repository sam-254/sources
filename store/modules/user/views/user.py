from jinja2 import Markup

from store.core.view import BaseView
from store.modules.user.validators import Password

from wtforms import PasswordField
from wtforms.validators import DataRequired, Email


class UserView(BaseView):
    column_sortable_list = ('id', 'name', 'age',)
    column_editable_list = ('name',)

    column_exclude_list = ('password_hash',)
    form_excluded_columns = ('password_hash',)

    def scaffold_form(self, validators=True):
        form_class = super(UserView, self).scaffold_form()
        form_class.password = PasswordField('password', [DataRequired(), Password()])

        return form_class

    def create_form(self, obj=None):
        form = super(UserView, self).create_form(obj)

        form.password_hash = form.password

        return form

    form_args = dict(
        name=dict(label='name', validators=[DataRequired()]),
        email=dict(label="Email", validators=[Email(), DataRequired()]),
    )

    def _list_thumbnail(view, context, model, name):
        if not model.geolocation:
            return ''
        return Markup(
            f'<div style="display: flex; justify-content: center">'
            f'<img src="https://www.countryflags.io/{model.geolocation.lower()}/flat/64.png"></div>'
        )

    column_formatters = {
        'geolocation': _list_thumbnail
    }
