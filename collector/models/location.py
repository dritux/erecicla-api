from collector import db, ma


class Location(db.Model):

    __tablename__ = 'location'

    location_id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String(15), unique=False)
    street = db.Column(db.String(100), unique=False)
    number = db.Column(db.String(10), unique=False)
    state = db.Column(db.String(50), unique=False)
    city = db.Column(db.String(50), unique=False)
    country = db.Column(db.String(30), unique=False)
    additional = db.Column(db.String(50), unique=False)
    latitude = db.Column(db.String(20), unique=False)
    longitude = db.Column(db.String(20), unique=False)
    type = db.Column(db.String(30), unique=False)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())

    def __init__(
        self,
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
    ):
        self.zipcode = zipcode
        self.street = street
        self.number = number
        self.state = state
        self.city = city
        self.country = country
        self.additional = additional
        self.latitude = latitude
        self.longitude = longitude
        self.type = type

    def __repr__(self):
        return '<Location %r>' % self.street


class LocationSchema(ma.Schema):
    class Meta:
        fields = (
            'location_id',
            'zipcode',
            'street',
            'number',
            'state',
            'city',
            'country',
            'additional',
            'latitude',
            'longitude',
            'type',
            'create_at',
            'update_at'
        )


location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)
