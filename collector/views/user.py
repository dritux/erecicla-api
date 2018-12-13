from flask import Blueprint, jsonify, request
from collector.models import User, Location, users_schema, user_schema
from collector import db

user = Blueprint('user', __name__, url_prefix='')


@user.route("/user", methods=['GET'])
def get():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


@user.route('/user', methods=['POST'])
def create():
    name = request.json['name']
    nickname = request.json['nickname']
    picture = request.json['picture']
    phone = request.json['phone']
    cellphone = request.json['cellphone']
    email = request.json['email']
    personal_code = request.json['personal_code']
    gender = request.json['gender']
    birthday = request.json['birthday']
    zipcode = request.json['zipcode']
    street = request.json['street']
    number = request.json['number']
    state = request.json['state']
    city = request.json['city']
    country = request.json['country']
    additional = request.json['additional']
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    type = request.json['type']

    location = Location(
        zipcode,
        street,
        number,
        state,
        city,
        country,
        additional,
        latitude,
        longitude,
        type
    )
    db.session.add(location)

    user = User(
        location.location_id,
        name,
        nickname,
        picture,
        phone,
        cellphone,
        email,
        personal_code,
        gender,
        birthday
    )
    db.session.add(user)
    db.session.commit()

    return user_schema.jsonify(user)
