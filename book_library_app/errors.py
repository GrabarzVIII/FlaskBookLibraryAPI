from flask import Response, jsonify
from book_library_app import app, db


class ErrorResponse:
    def __init__(self, message: str, http_status: int):
        self.playload = {
            'success': False,
            'message': message
        }
        self.http_status = http_status
        
    def to_response(self) -> Response:
        response = jsonify(self.playload)
        response.status_code = self.http_status
        return response

@app.errorhandler(404)
def not_found_error(error):
    return ErrorResponse(error.description, 404).to_response()

@app.errorhandler(400)
def wrong_request_error(error):
    messages = error.data.get('messages', {}).get('json', {})
    return ErrorResponse(messages, 400).to_response()

@app.errorhandler(415)
def unsupported_media_type_error(error):
    return ErrorResponse(error.description, 415).to_response()

@app.errorhandler(500)
def internal_server_error(error):
    db.session.rollback()
    return ErrorResponse(error.description, 500).to_response()
