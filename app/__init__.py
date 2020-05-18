import os
from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serialize import configure as config_ma

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
        os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .models.Books import bp_books
    app.register_blueprint(bp_books)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
