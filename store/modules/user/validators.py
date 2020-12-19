from wtforms import ValidationError


class Password(object):
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        password = field.data

        message = self.message
        if message is None:
            message = field.gettext('Invalid password')

        if len(password) < 6:
            raise ValidationError(message)
