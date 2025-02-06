from ..extensions import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from .post import Post

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship(Post, backref='author', lazy='dynamic')
    status = db.Column(db.String(150), default="user")
    name = db.Column(db.String(150), unique=True, nullable=False)
    login = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date = db.Column(db.DateTime, default=datetime.now())
    # avatar = db.Column(db.String(2000), nullable=True)
