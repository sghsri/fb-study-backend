from flask_session import Session
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import os


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///:memory:"
)
Session(app)
CORS(app)


WHITELIST = ['192.168.1.', '127.0.0.1', 'stroudresearch.net']


@app.errorhandler(403)
def permission_error(e):
    return "Invalid Permissions."


@app.before_request
def limit_remote_addr():
    client_ip = str(request.remote_addr)
    client_host = str(request.host)
    print(client_ip + " " + client_host)
    valid = False
    for origin in WHITELIST:
        if client_ip.startswith(origin) or client_ip == origin or origin in client_host:
            valid = True
            break
    if not valid:
        abort(403)
