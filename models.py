# models.py

from config import db, ma


class User(db.Model):
    __tablename__ = "users"
    userID = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)
    serverID = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    avatar = db.Column(db.String(200), nullable=False)

class Album(db.Model):
    __tablename__ = "albums"
    albumID = db.Column(db.String(20), unique=True, nullable=False, primary_key=True)
    artist = db.Column(db.String(20), nullable=False)
    album = db.Column(db.String(20), nullable=False)
    albumImage = db.Column(db.String(200), nullable=False)
    medianScore = db.Column(db.String(2), nullable=False)

class Review(db.Model):
    __tablename__ = "reviews"
    userID = db.Column(db.String(20), db.ForeignKey("users.userID"), primary_key=True, nullable=False)
    albumID = db.Column(db.String(20), db.ForeignKey("albums.albumID"), primary_key=True, nullable=False)
    score = db.Column(db.String(2), nullable=False)
    review = db.Column(db.String(1000), nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

class AlbumSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Album
        load_instance = True
        sqla_session = db.session

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        sqla_session = db.session
        include_fk = True

user_schema = UserSchema()
album_schema = AlbumSchema()
review_schema = ReviewSchema()
users_schema = UserSchema(many=True)
albums_schema = AlbumSchema(many=True)
reviews_schema = ReviewSchema(many=True)