#models.py

from config import db, ma


class Reviews(db.Model):
    __tablename__ = "review"
    id = db.Column(db.Integer, primary_key=True)
    reviewID = db.Column(db.String(20), unique=True)
    reviewerID = db.Column(db.String(20))
    serverID = db.Column(db.String(20))
    artista = db.Column(db.String(20))
    album = db.Column(db.String(20))
    albumImage = db.Column(db.String(200))
    score = db.Column(db.Integer)
    review = db.Column(db.String(1000))
    
class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reviews
        load_instance = True
        sqla_session = db.session
        
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)