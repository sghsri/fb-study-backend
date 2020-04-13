from flask import Blueprint, jsonify, request, session
import json
import bcrypt
from sample_data.sample_db import sample_db, validate_input

job_routes = Blueprint("job_routes", __name__)


@job_routes.route("/data")
def index():
    jobs = sample_db.read_jobs()
    return jsonify(jobs)


@job_routes.route("/data/<field>/<position>")
def data_for_field_position(field, position):
    jobs = sample_db.read_jobs()
    return jsonify(jobs)


@job_routes.route("/submit_data", methods=["POST"])
def submit_data():
    data = request.get_json()
    if(data):
        data['hello'] = 'world'
        return jsonify(data)
    return "There was an issue with the data being submitted."
