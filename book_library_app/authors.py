from flask import jsonify, request
from book_library_app import app, db
from book_library_app.models import Author, AuthorSchema, author_schema
from webargs.flaskparser import use_args
from book_library_app.utils import validate_json_content_type


@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    author_schema = AuthorSchema(many=True)

    return jsonify({
        'success': True,
        'data': author_schema.dump(authors),
        'number_of_records': len(authors)
    })

@app.route('/api/v1/authors/<int:author_id>', methods=['GET'])
def get_author(author_id: int):
    author = Author.query.get_or_404(author_id, description=f"Author with id {author_id} not found")
    return jsonify({
        'success': True,
        'data': author_schema.dump(author)
    })

@app.route('/api/v1/authors', methods=['POST'])
@validate_json_content_type
@use_args(author_schema, error_status_code=400)
def creat_author(args: dict):
    print(args)
    # data = request.get_json()
    # first_name = data.get('first_name')
    # last_name = data.get('last_name')
    # birth_date = data.get('birth_date')
    # author = Author(first_name=first_name, last_name=last_name, birth_date=birth_date)
    author = Author(**args)
    db.session.add(author)
    db.session.commit()
    # print(author)
    return jsonify({
        'success': True,
        'data': author_schema.dump(author)
    }), 201

@app.route('/api/v1/authors/<int:author_id>', methods=['PUT'])
def update_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Singel author has been updated with id {author_id}'
    })

@app.route('/api/v1/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Deleted singel author with id {author_id}'
    })

print("END")