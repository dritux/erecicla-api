from collector import db, ma


class User(db.Model):

    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False)
    nickname = db.Column(db.String(45), unique=False)
    picture = db.Column(db.String(255), unique=False)
    phone = db.Column(db.String(14), unique=True)
    cellphone = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(100), unique=True)
    personal_code = db.Column(db.String(30), unique=True)
    gender = db.Column(db.String(1), unique=False)
    birthday = db.Column(db.String(10), unique=False)
    create_at = db.Column(db.DateTime())
    update_at = db.Column(db.DateTime())

    def __init__(
        self,
        name,
        nickname,
        picture,
        phone,
        cellphone,
        email,
        personal_code,
        gender,
        birthday,
        create_at,
        update_at
    ):
        self.name = name
        self.nickname = nickname
        self.picture = picture
        self.phone = phone
        self.cellphone = cellphone
        self.email = email
        self.personal_code = personal_code
        self.gender = gender
        self.birthday = birthday
        self.create_at = create_at
        self.update_at = update_at

    def __repr__(self):
        return '<User %r>' % self.name


class UserSchema(ma.Schema):
    class Meta:
        fields = (
            'name',
            'nickname',
            'picture',
            'phone',
            'cellphone',
            'email',
            'personal_code',
            'gender',
            'birthday',
            'create_at',
            'update_at'
        )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
