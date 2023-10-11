import random
import string

from config import db
from models import Reviews, review_schema, reviews_schema

def generate_random_string(length=20):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits

    # Generate the random string
    random_string = ''.join(random.choice(characters) for i in range(length))
    
    # Checks if exists
#    while True:
#        if Reviews.query.filter(Reviews.reviewID == random_string).one_or_none() is not None:
#            random_string = ''.join(random.choice(characters) for i in range(length))
#        else:
#            break

    # Return the random string
    return random_string