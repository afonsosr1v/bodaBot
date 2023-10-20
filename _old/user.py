# Description: This file contains the routes for the user blueprint.
# user.py

from flask import abort,  make_response

from rsg import generate_random_string as rsg
from config import db
from models import User, user_schema, users_schema, users_and_relations_schema
from models import Review, review_schema, reviews_schema


def read_all():
    users = User.query.all()
    return users_schema.dump(users)

def read_all_with_reviews():

    users = User.query.all()
    return users_and_relations_schema.dump(users)

def read_userID(userID):
    user = User.query.filter(User.userID == userID).one_or_none()
    
    if user is not None:
        return user_schema.dump(user)
    else:
        abort(
            404, f"Review with ID {userID} not found"
        )

def read_user_reviews(userID):
    user = User.query.filter(User.userID == userID).one_or_none()
    
    if user is not None:
        reviews = Review.query.filter(Review.userID == userID).all()
        return reviews_schema.dump(reviews)
    else:
        abort(
            404, f"Review with ID {userID} not found"
        )

def create(userName):
    existing_user = User.query.filter(User.userName == userName).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(userName, session=db.session)
        new_user.userID = rsg(20)
        new_user.serverID = rsg(20)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(
            406,
            f"User with name {userName} already exists",
        )