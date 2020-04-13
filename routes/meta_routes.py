from flask import Blueprint, jsonify, request, session

meta_routes = Blueprint("meta_routes", __name__)


@meta_routes.route("/")
def index():
    print("hello world")
    return "Hello this is the apply.fyi backend"
