#models.py

from config import db, ma
from marshmallow_sqlalchemy import fields

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20), nullable=False)
    userID = db.Column(db.String(20), unique=True, nullable=False)
    serverID = db.Column(db.String(20), nullable=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    reviewID = db.Column(db.String(20), unique=True, nullable=False)
    userID = db.Column(db.String(20), db.ForeignKey("users.userID"), nullable=False)
#    serverID = db.Column(db.String(20), nullable=False)
    artista = db.Column(db.String(20), nullable=False)
    album = db.Column(db.String(20), nullable=False)
    albumImage = db.Column(db.String(200), nullable=False)
    score = db.Column(db.String(2), nullable=False)
    review = db.Column(db.String(1000), nullable=False)

    users = db.relationship(
        "User", 
        backref="reviews",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        lazy=True
        )


class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        sqla_session = db.session
        include_fk = True


class UserAndRelationsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
        include_fk = True

    reviews = fields.Nested(ReviewSchema, many=True)    

        
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
users_and_relations_schema = UserAndRelationsSchema(many=True)