# Description: This file contains all the functions that are used for development putposes.
# temp_funmctions.py

from config import db
from models import User, user_schema, users_schema, users_and_relations_schema
from models import Review, review_schema, reviews_schema
from rsg import generate_random_string as rsg


def check_if_user_exists(userID):
    existing_user = User.query.filter(User.userID == userID).one_or_none()
    if existing_user is not None:
        return True
    else:
        return False
    
def generate_username():
    return rsg(7)