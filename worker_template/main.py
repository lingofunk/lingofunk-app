from flask import Flask, request, jsonify
import logging
import sys
app = Flask(__name__)

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@app.route('/vectorize', methods=['POST'])
def vectorize():
    # request should be json with data from web-ui
    logger.debug(request.get_json())
    data = request.get_json()
    return jsonify(
        tokenized_text=data.get('text', 'Smth wrong').split(),
        attention_map=[0.9, 0.1]
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
