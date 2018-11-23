from collector import db, ma


class User(db.Model):

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(120), unique=True)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return '<User %r>' % self.username


class UserSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email', 'phone')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
