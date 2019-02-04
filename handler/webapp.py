from flask import send_from_directory, jsonify, request


class Webapp:
    def __init__(self):
        pass

    def get_page(self):
        return send_from_directory('.', 'index.html')

    def render_response(self, response):
        # TODO
        return

    def get_request_data(self):
        # TODO
        return {
            "task": "classify-text",
            "args": {
                "text": request.form['input-text']
            }
        }

    def _test(self):
        return jsonify({'status': 'ok'}), 200
