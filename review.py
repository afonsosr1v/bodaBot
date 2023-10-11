# review.py

from rng import generate_random_string
from flask import abort,  make_response

REVIEW = {
    "1": {
        "reviewID": "1",
        "reviewerID": "1",
        "serverID": "1",
        "artista": "a",
        "album": "b",
        "albumImage": "ya",
        "score": "c",
        "review": "d",
    },
    "2": {
        "reviewID": "2",
        "reviewerID": "1",
        "serverID": "1",
        "artista": "A",
        "album": "B",
        "albumImage": "ya",
        "score": "C",
        "review": "D",
    },
    "3": {
        "reviewID": "3",
        "reviewerID": "1",
        "serverID": "1",
        "artista": "AA",
        "album": "BB",
        "albumImage": "ya",
        "score": "CC",
        "review": "DD",
    }
}

def read_all():
    return list(REVIEW.values())

def create(review):
    reviewID = generate_random_string()
    reviewerID = "1"
    serverID = "1"
    artista = review.get("artista")
    album = review.get("album")
    albumImage = "ya"
    score = review.get("score")
    review = review.get("review")

    if reviewerID and artista and album not in REVIEW:
        REVIEW[reviewID] = {
            "reviewID": reviewID,
            "reviewerID": reviewerID,
            "serverID": serverID,
            "artista": artista,
            "album": album,
            "albumImage": albumImage,
            "score": score,
            "review": review,
        }
        return REVIEW[reviewID], 201
    else:
        abort(
            406,
            f"Review for {album} already exists",
        )

def read_reviewID(reviewID):
    if reviewID in REVIEW:
        return REVIEW[reviewID]
    else:
        abort(
            404, f"Review with ID {reviewID} not found"
        )

def delete(reviewID):
    if reviewID in REVIEW:
        del REVIEW[reviewID]
        return make_response(
            f"{reviewID} apagado com sucesso", 200
        )
    else:
        abort(
            404,
            f"Review {reviewID} não encontrada"
        )