from store.extensions import *


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_elements(cls):
        print("________________________________________", cls.query.all)
        return

    @classmethod
    def get_category(cls):
        try:
            return cls.__category__
        except Exception as e:
            return ''
