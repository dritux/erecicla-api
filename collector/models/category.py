from collector import db, ma


class Category(db.Model):

    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)

    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


class Categorieschema(ma.Schema):
    class Meta:
        fields = ('category_id', 'name',)


category_schema = Categorieschema()
categories_schema = Categorieschema(many=True)
