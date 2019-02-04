import sys, os

sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..'
    )
)

import argparse
from flask import Flask, Response, send_from_directory, request, jsonify

from handler.tasks import task_test


app = Flask(__name__, static_url_path='')


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return send_from_directory('.', 'index.html')


@app.route('/test', methods=['POST'])
def index():
    task = task_test.s().delay()
    return jsonify({'id': '', 'status': ''}), 201


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
           '--port', type=int, default=8001,
           help='The port to listen on (default is 8001).')
    args = parser.parse_args()

    INSIDE_DOCKER = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)
    host = '0.0.0.0' if INSIDE_DOCKER else 'localhost'

    app.run(host=host, port=args.port, debug=True, threaded=True)
