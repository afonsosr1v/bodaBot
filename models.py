#models.py

from config import db, ma

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(20), unique=True)
    serverID = db.Column(db.String(20))

"""     reviews = db.relationship(
        "Reviews", 
        backref="users",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        lazy=True
        ) """

class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    reviewID = db.Column(db.String(20), unique=True)
    reviewerID = db.Column(db.String(20), db.ForeignKey("users.userID"))
#    serverID = db.Column(db.String(20))
    artista = db.Column(db.String(20))
    album = db.Column(db.String(20))
    albumImage = db.Column(db.String(200))
    score = db.Column(db.String(2))
    review = db.Column(db.String(1000))

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
        
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)