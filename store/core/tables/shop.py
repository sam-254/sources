from store.extensions import db


shops_shipcountries_relation = db.Table(
    'countries_shops',
    db.Column('shop_id', db.Integer(), db.ForeignKey('shop.id')),
    db.Column('country_id', db.Integer(), db.ForeignKey('country.id')))
