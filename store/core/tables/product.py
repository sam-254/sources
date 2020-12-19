from store.extensions import db


metafield_self_relation = db.Table(
    'metafield_relation',
    db.Column('my_id', db.Integer, db.ForeignKey('metafield.id')),
    db.Column('my_parent_id', db.Integer, db.ForeignKey('metafield.id'))
)

options_products_relation = db.Table(
    'options_products',
    db.Column('product_id', db.Integer(), db.ForeignKey('product.id')),
    db.Column('option_id', db.Integer(), db.ForeignKey('option.id')))

tags_products_relation = db.Table(
    'tags_products',
    db.Column('product_id', db.Integer(), db.ForeignKey('product.id')),
    db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id')))

selected_options_products_relation = db.Table(
    'selectedinput_products',
    db.Column('product_id', db.Integer(), db.ForeignKey('product.id')),
    db.Column('selectedinput_id', db.Integer(), db.ForeignKey('selectedinput.id')))


images_options_relation = db.Table(
    'images_options',
    db.Column('variantoptinos_id', db.Integer(), db.ForeignKey('variantoptions.id')),
    db.Column('image_id', db.Integer(), db.ForeignKey('image.id')))

variants_options_relation = db.Table(
    'variant_options',
    db.Column('variantoptinos_id', db.Integer(), db.ForeignKey('variantoptions.id')),
    db.Column('option_id', db.Integer(), db.ForeignKey('option.id')))
