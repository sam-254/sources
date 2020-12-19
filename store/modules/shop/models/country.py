from store.core.model import Base
from store.core.mixins import DateTimeMixin
from store.extensions import db


class Country(Base, DateTimeMixin):
    __category__ = 'Shop'

    name = db.Column(db.String(255), nullable=False)
