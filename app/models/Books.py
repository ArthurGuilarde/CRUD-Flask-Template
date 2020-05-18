from flask import Blueprint, current_app, request, jsonify
from ..model import Books
from ..serialize import BookSchema

bp_books = Blueprint('books', __name__)


@bp_books.route('/show', methods=['GET'])
def show():
    bs = BookSchema(many=True)
    result = Books.query.all()
    return bs.jsonify(result), 200


@bp_books.route('/add', methods=['POST'])
def add():
    bs = BookSchema()
    book = bs.load(request.json)

    current_app.db.session.add(book)
    current_app.db.session.commit()

    return bs.jsonify(book), 201


@bp_books.route('/update/<id>', methods=['PUT'])
def update(id):
    bs = BookSchema()
    query = Books.query.filter(Books.id == id)
    query.update(request.json)
    current_app.db.session.commit()

    return bs.jsonify(query.first())


@bp_books.route('/remove/<id>', methods=['DELETE'])
def remove(id):
    Books.query.filter(Books.id == id).delete()
    current_app.db.session.commit()

    return jsonify('Deleted')
