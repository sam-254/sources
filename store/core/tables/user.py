from store.extensions import db

friend_relation = db.Table(
    'friend_relation',
    db.Column('my_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('my_friends_id', db.Integer, db.ForeignKey('user.id'))
)
best_fried_relation = db.Table(
    'best_fried_relation',
    db.Column('my_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('my_friends_id', db.Integer, db.ForeignKey('user.id'))
)

roles_users_relation = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))
