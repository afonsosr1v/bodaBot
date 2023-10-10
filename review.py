# review.py

from rng import generate_random_string
from flask import abort

REVIEW = {
    generate_random_string(): {
        "artista": "a",
        "album": "b",
        "score": "c",
        "review": "d",
    },
    generate_random_string(): {
        "artista": "A",
        "album": "B",
        "score": "C",
        "review": "D",
    },
    generate_random_string(): {
        "artista": "AA",
        "album": "BB",
        "score": "CC",
        "review": "DD",
    }
}

def read_all():
    return list(REVIEW.values())

def create(review):
    artista = review.get("artista")
    album = review.get("album")
    score = review.get("score")
    review = review.get("review", "")
    Id = generate_random_string()

    if artista and album not in REVIEW:
        REVIEW[Id] = {
            "artista": artista,
            "album": album,
            "score": score,
            "review": review,
        }
        return REVIEW[Id], 201
    else:
        abort(
            406,
            f"Album {album} already exists",
        )
