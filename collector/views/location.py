from flask import Blueprint, jsonify

from collector.models import Location, locations_schema


location = Blueprint('location', __name__, url_prefix='')


@location.route("/locations", methods=['GET'])
def get_locations():
    all_locations = Location.query.all()
    result = locations_schema.dump(all_locations)
    return jsonify(result.data)
