from flask import Blueprint, jsonify, request, session
import json
import bcrypt
from database.db import db

post_routes = Blueprint("post_routes", __name__)


@post_routes.route("/api/posts")
def index():
    posts = db.read_posts()
    return jsonify(posts)
