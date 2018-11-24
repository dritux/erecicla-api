from collector import db, ma


class Collector(db.Model):

    __tablename__ = 'collector'

    collector_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.user_id'),
        nullable=False
    )
    type = db.Column(db.String(30), unique=False)

    def __init__(self, user_id, type):
        self.user_id = user_id
        self.type = type

    def __repr__(self):
        return '<Collector %r>' % self.user_id


class CollectorSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'type')


collector_schema = CollectorSchema()
collectors_schema = CollectorSchema(many=True)
