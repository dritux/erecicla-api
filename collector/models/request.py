from collector import db, ma


class Request(db.Model):

    __tablename__ = 'request'

    request_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.user_id'),
        nullable=False
    )
    collection_id = db.Column(
        db.Integer,
        db.ForeignKey('collection.collection_id'),
        nullable=False
    )
    collector_id = db.Column(
        db.Integer,
        db.ForeignKey('collector.collector_id'),
        nullable=False
    )
    location_id = db.Column(
        db.Integer,
        db.ForeignKey('location.location_id'),
        nullable=False
    )
    scheduled_start = db.Column(db.Time())
    scheduled_end = db.Column(db.Time())
    scheduled_at = db.Column(db.DateTime())
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())
    accept_at = db.Column(db.DateTime())

    def __init__(
        self,
        request_id,
        user_id,
        collection_id,
        collector_id,
        location_id,
        scheduled_start,
        scheduled_end,
        scheduled_at,
        create_at,
        update_at,
        accept_at
    ):
        self.request_id = request_id
        self.user_id = user_id
        self.collection_id = collection_id
        self.collector_id = collector_id
        self.location_id = location_id
        self.scheduled_start = scheduled_start
        self.scheduled_end = scheduled_end
        self.scheduled_at = scheduled_at
        self.create_at = create_at
        self.update_at = update_at
        self.accept_at = accept_at

    def __repr__(self):
        return '<Request %r>' % self.request_id


class RequestSchema(ma.Schema):
    class Meta:
        fields = (
            'request_id',
            'user_id',
            'collection_id',
            'collector_id',
            'location_id',
            'scheduled_start',
            'scheduled_end',
            'scheduled_at',
            'create_at',
            'update_at',
            'accept_at'
        )


request_schema = RequestSchema()
requests_schema = RequestSchema(many=True)
