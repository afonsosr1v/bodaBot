# review.py

from flask import abort,  make_response

from rsg import generate_random_string as rsg
from config import db
from models import Reviews, review_schema, reviews_schema



def read_all():
    reviews = Reviews.query.all()
    return reviews_schema.dump(reviews)

def create(review):
    reviewerID = review.get("reviewerID")
    artista = review.get("artista")
    album = review.get("album")
    
    existing_review = Reviews.query.filter(Reviews.reviewerID == reviewerID, Reviews.artista == artista, Reviews.album == album).one_or_none()

    if existing_review is None:
        new_review = review_schema.load(review, session=db.session)
        new_review.reviewerID = rsg(20)
        new_review.serverID = rsg(20)
        new_review.albumImage = rsg(20)
        
        new_review.reviewID = rsg(20)
        while Reviews.query.filter(Reviews.reviewID == new_review.reviewID).one_or_none(): 
            new_review.reviewID = rsg(20)
        
        db.session.add(new_review)
        db.session.commit()
        return review_schema.dump(new_review), 201
    else:
        abort(
            406,
            f"Review for {album} by {artista} already exists",
        )

def read_reviewID(reviewID):
    existing_review = Reviews.query.filter(Reviews.reviewID == reviewID).one_or_none()
    
    if existing_review is not None:
        return review_schema.dump(existing_review)
    else:
        abort(
            404, f"Review with ID {reviewID} not found"
        )

def delete(reviewID):
    existing_review = Reviews.query.filter(Reviews.reviewID == reviewID).one_or_none()
    
    if existing_review:
        db.session.delete(existing_review)
        db.session.commit()
        return make_response(
            f"{reviewID} apagado com sucesso", 200
        )
    else:
        abort(
            404,
            f"Review {reviewID} não encontrada"
        )