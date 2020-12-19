from store.extensions import db


class NameMixin:
    name = db.Column(db.String())

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()


class DateTimeMixin:
    created_at = db.Column(db.DateTime(), default=db.func.now())
    updated_at = db.Column(db.DateTime(), onupdate=db.func.now())


class AdminViewMixin():
    pass
