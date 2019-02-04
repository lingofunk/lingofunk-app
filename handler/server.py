import sys, os
import argparse
from flask import Flask

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
)

from handler.worker import Worker
from handler.webapp import Webapp


app = Flask(__name__, static_url_path='')
worker = Worker()
webapp = Webapp()


@app.route('/', methods=('GET',))
@app.route('/classify-text', methods=('GET',))
@app.route('/generate-text', methods=('GET',))
@app.route('/transform-text', methods=('GET',))
def get():
    return webapp.get_page()


@app.route('/', methods=('POST',))
@app.route('/classify-text', methods=('POST',))
@app.route('/generate-text', methods=('POST',))
@app.route('/transform-text', methods=('POST',))
def post():
    request = webapp.get_request_data()
    response = worker.process_request(request)
    webapp.render_response(response)

    # TODO

    return webapp.get_page()


@app.route('/test', methods=('POST', 'GET'))
def test():
    return webapp._test()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
           '--port', type=int, default=8001,
           help='The port to listen on (default is 8001).')
    args = parser.parse_args()

    INSIDE_DOCKER = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)
    host = '0.0.0.0' if INSIDE_DOCKER else 'localhost'

    app.run(host=host, port=args.port, debug=True, threaded=True)
