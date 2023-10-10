import random
import string

def generate_random_string(length=20):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits

    # Generate the random string
    random_string = ''.join(random.choice(characters) for i in range(length))

    # Return the random string
    return random_string