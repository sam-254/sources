from store.core.model import Base
from store.extensions import db
from store.core.mixins import DateTimeMixin


class Tag(Base, DateTimeMixin):
    __category__ = 'Product'

    name = db.Column(db.String(255), nullable=False)
