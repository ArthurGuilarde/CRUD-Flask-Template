from flask_marshmallow import Marshmallow
from .model import Books

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Books
        load_instance = True
