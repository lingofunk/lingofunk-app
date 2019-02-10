import argparse
from flask import Flask, Response, render_template, request
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import logging
import sys


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=8000)
    parser.add_argument("--host", default="0.0.0.0")
    return parser.parse_args()


# https://www.peterbe.com/plog/best-practice-with-retries-with-requests
def requests_retry_session(retries=4,
                           backoff_factor=1,
                           status_forcelist=(500, 502, 504),
                           session=None):
    session = session or requests.Session()

    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        status=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )

    adapter = HTTPAdapter(max_retries=retry)

    session.mount('http://', adapter)
    session.mount('https://', adapter)

    return session


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/classify-sentiment")
def classify_sentiment():
    return render_template("lingofunk-classify-sentiment.html")


@app.route("/generate/discrete")
def generate_discrete():
    return render_template("lingofunk-generate-discrete.html")


@app.route("/generate/continuous")
def generate_continuous():
    return render_template("lingofunk-generate-continuous.html")


@app.route("/transfer-style")
def transfer():
    return render_template("lingofunk-transfer.html")


@app.route("/api/classifier/activations", methods=["GET", "POST"])
def activations_api():
    msg = f"Got {request.get_json()}, resent to the binary sentiment classifier"
    logger.debug(msg)
    response = requests.post(
        "http://sentiment-classifier:8000/activations", json=request.get_json()
    )
    return Response(response.content, response.status_code)


@app.route("/api/generator/discrete", methods=["GET", "POST"])
def api_generator_discrete():
    msg = f"API proxy got {request.get_json()}, resent to the generator"
    logger.debug(msg)

    response = requests_retry_session().post("http://generator:8000/generate/discrete", json=request.get_json())

    return Response(response.content, response.status_code)

# TODO: DRY
@app.route("/api/generator/continuous", methods=["GET", "POST"])
def api_generator_continuous():
    msg = f"API proxy got {request.get_json()}, resent to the generator"
    logger.debug(msg)

    response = requests_retry_session().post("http://generator:8000/generate/continuous", json=request.get_json())

    return Response(response.content, response.status_code)


@app.route("/api/transferrer", methods=["GET", "POST"])
def api_transferrer():
    data = request.get_json()
    msg = f"API proxy got {data}, resent to the transferrer"
    logger.debug(msg)

    response = requests.post("http://transferrer:8000/api/transfer", json=data)

    return Response(response.content, response.status_code)


# # todo: make all demos generic
# @app.route('/worker_demo')
# def worker_demo():
#     return render_template('worker_demo.html')


# # todo: make worker_one generic argument and redirect blindly
# @app.route('/api/worker_one/vectorize', methods=['POST'])
# def api_worker():
#     msg = 'API proxy got {} resend to worker'.format(request.get_json())
#     logger.debug(msg)
#     response = requests.post(
#         'http://worker_one:8000/vectorize',
#         json=request.get_json())
#     return Response(response.content, response.status_code)


if __name__ == "__main__":
    args = _parse_args()
    app.run(**args.__dict__)
