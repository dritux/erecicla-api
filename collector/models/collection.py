from collector import db, ma


class Collection(db.Model):

    __tablename__ = 'collection'

    collection_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey('category.category_id'),
        nullable=False
    )
    collector_id = db.Column(
        db.Integer,
        db.ForeignKey('collector.collector_id'),
        nullable=False
    )
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())

    def __init__(
        self,
        collection_id,
        category_id,
        collector_id,
        create_at,
        update_at
    ):
        self.collection_id = collection_id
        self.category_id = category_id
        self.collector_id = collector_id
        self.create_at = create_at
        self.update_at = update_at

    def __repr__(self):
        return '<Collection %r>' % self.collection_id


class CollectionSchema(ma.Schema):
    class Meta:
        fields = (
            'collection_id',
            'category_id',
            'collector_id',
            'create_at',
            'update_at'
        )


collection_schema = CollectionSchema()
collections_schema = CollectionSchema(many=True)
