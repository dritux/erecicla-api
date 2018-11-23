from flask import Blueprint, jsonify

from collector.models import User, users_schema


user = Blueprint('user', __name__, url_prefix='')


@user.route("/users", methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)
