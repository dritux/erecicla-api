from flask import Blueprint, jsonify

from collector.models import Category, categories_schema


category = Blueprint('category', __name__, url_prefix='')


@category.route("/categories", methods=['GET'])
def get_categories():
    all_categories = Category.query.all()
    result = categories_schema.dump(all_categories)
    return jsonify(result.data)
