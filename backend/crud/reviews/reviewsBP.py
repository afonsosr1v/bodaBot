# reviewsBP.py

from flask import Blueprint, request, jsonify
from config import db
from models import Review, review_schema, reviews_schema

reviewsBP = Blueprint('reviewsBP', __name__, url_prefix="/reviews")

@reviewsBP.route('/create', methods=["POST"])
def create_review():
    if not request.json:
        return jsonify({'error': 'No JSON payload received'}), 400

    userID = request.json.get('userID')
    albumID = request.json.get('albumID')
    score = request.json.get('score')
    review = request.json.get('review')

    if not all([userID, albumID, score, review]):
        return jsonify({'error': 'Missing required fields'}), 400

    new_review = Review()
    new_review.userID = userID
    new_review.albumID = albumID
    new_review.score = score
    new_review.review = review

    db.session.add(new_review)
    db.session.commit()

    return review_schema.jsonify(new_review)

@reviewsBP.route('/get', methods=["GET"])
def get_reviews():
    all_reviews = Review.query.all()
    result = reviews_schema.dump(all_reviews)
    return jsonify(result)

@reviewsBP.route('/get/<userID>', methods=["GET"])
def get_review(userID):
    review = Review.query.get(userID)
    return review_schema.jsonify(review)

@reviewsBP.route('/update/<userID>', methods=["PUT"])
def update_review(userID):
    review = Review.query.filter_by(userID=userID).one_or_none()

    if not review:
        return jsonify({'error': 'Review not found'}), 404

    if request.json is not None:
        review.userID = request.json.get('userID')
        review.albumID = request.json.get('albumID')
        review.score = request.json.get('score')
        review.review = request.json.get('review')

    db.session.commit()

    return review_schema.jsonify(review)

@reviewsBP.route('/delete/<userID>', methods=["DELETE"])
def delete_review(userID):
    review = Review.query.filter_by(userID=userID).one_or_none()

    if not review:
        return jsonify({'error': 'Review not found'}), 404

    db.session.delete(review)
    db.session.commit()

    return jsonify({'success': 'Review deleted'}), 200

