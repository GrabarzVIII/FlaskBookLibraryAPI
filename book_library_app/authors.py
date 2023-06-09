from flask import jsonify
from book_library_app import app



@app.route('/api/v1/authors', methods=['GET'])
def get_authors():
    return jsonify({
        'success': True,
        'data': 'Get all authors'
    })

@app.route('/api/v1/authors/<int:author_id>', methods=['GET'])
def get_author(author_id: int):
    return jsonify({
        'success': True,
        'data': f'Get singel author with id {author_id}'
    })

@app.route('/api/v1/authors', methods=['POST'])
def creat_author():
    return jsonify({
        'success': True,
        'data': 'New author has been created'
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