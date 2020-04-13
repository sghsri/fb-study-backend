from flask import Blueprint, jsonify, request, session
import bcrypt

meta_routes = Blueprint("meta_routes", __name__)


@meta_routes.route("/")
def index():
    print("hello world")
    return "Hello this is the apply.fyi backend"


@meta_routes.route("/api/auth", methods=["POST"])
def do_auth():
    abc123_hash = b"$2b$12$ljDi4EMFQSVn65YQsGbQCuhxIfyanbO3f9niGW1b5cskulmK6GG96"
    data = request.get_json()
    passw = data["password"]
    user_id = data["id"]
    if bcrypt.checkpw(password, hashed):
        session["user_id"] = user_id
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"})


@meta_routes.route("/api/logout", methods=["GET"])
def logout():
    session.pop("user_id")
    return jsonify({"status": "success"})
