from flask import Blueprint, jsonify

from collector.models import Collection, collections_schema


collection = Blueprint('collection', __name__, url_prefix='')


@collection.route("/collections", methods=['GET'])
def get_collections():
    all_collections = Collection.query.all()
    result = collections_schema.dump(all_collections)
    return jsonify(result.data)
