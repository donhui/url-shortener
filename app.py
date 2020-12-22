import random
import string
from flask import Flask, jsonify, request, abort, redirect
import redis
from settings import redis_settings
app = Flask(__name__)


def generate_identifier(n=6):
    identifier = ""
    for i in range(n):
        identifier += random.choice(string.ascii_letters)
    return identifier


def get_redis_instance():
    return redis.Redis(
        host=redis_settings.get('host'),
        port=redis_settings.get('port'),
        password=redis_settings.get('password'))


redis_instance = get_redis_instance()


@app.route("/")
def index():
    return "Hello, URL Shortener!"


@app.route("/generate/<path:address>/")
def generate(address):
    identifier = ''
    i = 0
    while True:
        if i == 20:
            break
        identifier = generate_identifier()
        if redis_instance.exists(identifier):
            i = i + 1
            continue
        else:
            break

    if identifier == '':
        return jsonify({"status": "fail", "error_msg": "generate shortened_url fail, please try again."})

    if not (address.startswith("http://") or address.startswith("https://")):
        address = "http://" + address

    redis_instance.set(identifier, address)

    shortened_url = request.host_url + identifier
    return jsonify({"identifier": identifier, "shortened_url": shortened_url})


@app.route("/<string:identifier>/")
def fetch_original(identifier):
    try:
        origin_url = redis_instance.get(identifier)
    except:
        abort(404)
    return redirect(origin_url)


@app.route("/restore/<string:identifier>/")
def restore(identifier):
    try:
        original_url = redis_instance.get(identifier)
    except:
        pass
    if original_url is None:
        return jsonify({"status": "fail", "error_msg": "get original_url fail, please check the identifier."})
    return jsonify({"identifier": identifier, "original_url": str(original_url)})


if __name__ == "__main__":
    app.run(debug=True)
