From flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return app.send_static_file('./index.html')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
           '--port', type=int, default=8001,
           help='The port to listen on (default is 8001).')
    args = parser.parse_args()
    INSIDE_DOCKER = os.environ.get('AM_I_IN_A_DOCKER_CONTAINER', False)
    host = "0.0.0.0" if INSIDE_DOCKER else "localhost"

    app.run(host='0.0.0.0', port=args.port, debug=True, threaded=True)
