from store.core.model import Base
from store.core.mixins import DateTimeMixin
from store.extensions import db

class Role(Base, DateTimeMixin):
    __category__ = 'User'

    name = db.Column(db.String(80), unique=True)
