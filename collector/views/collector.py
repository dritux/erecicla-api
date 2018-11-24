from flask import Blueprint, jsonify

from collector.models import Collector, collectors_schema


collector = Blueprint('collector', __name__, url_prefix='')


@collector.route("/collectors", methods=['GET'])
def get_collectors():
    all_collectors = Collector.query.all()
    result = collectors_schema.dump(all_collectors)
    return jsonify(result.data)
