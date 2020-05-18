from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import sqlalchemy as sq


db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Books(db.Model):
    id = sq.Column(sq.Integer, primary_key=True)
    book = sq.Column(sq.String(255))
    author = sq.Column(sq.String(255))
