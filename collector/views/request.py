from flask import Blueprint, jsonify

from collector.models import Request, requests_schema


request = Blueprint('request', __name__, url_prefix='')


@request.route("/requests", methods=['GET'])
def get_requests():
    all_requests = Request.query.all()
    result = requests_schema.dump(all_requests)
    return jsonify(result.data)
