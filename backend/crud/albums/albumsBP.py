# albumsBP.py

from flask import Blueprint, request, jsonify
from config import db
from models import Album, album_schema, albums_schema

albumsBP = Blueprint('albumsBP', __name__, url_prefix="/albums")

@albumsBP.route('/create', methods=["POST"])
def create_album():
    if not request.json:
        return jsonify({'error': 'No JSON payload received'}), 400

    albumID = request.json.get('albumID')
    artist = request.json.get('artist')
    album = request.json.get('album')
    albumImage = request.json.get('albumImage')
    medianScore = request.json.get('medianScore')

    if not all([albumID, artist, album, albumImage, medianScore]):
        return jsonify({'error': 'Missing required fields'}), 400

    new_album = Album()
    new_album.albumID = albumID
    new_album.artist = artist
    new_album.album = album
    new_album.albumImage = albumImage
    new_album.medianScore = medianScore

    db.session.add(new_album)
    db.session.commit()

    return album_schema.jsonify(new_album)

@albumsBP.route('/get', methods=["GET"])
def get_albums():
    all_albums = Album.query.all()
    result = albums_schema.dump(all_albums)
    return jsonify(result)

@albumsBP.route('/get/<albumID>', methods=["GET"])
def get_album(albumID):
    album = Album.query.get(albumID)
    return album_schema.jsonify(album)

@albumsBP.route('/update/<albumID>', methods=["PUT"])
def update_album(albumID):
    album = Album.query.filter_by(albumID=albumID).one_or_none()

    if not album:
        return jsonify({'error': 'Album not found'}), 404

    if request.json is not None:
        album.albumID = request.json.get('albumID')
        album.artist = request.json.get('artist')
        album.album = request.json.get('album')
        album.albumImage = request.json.get('albumImage')
        album.medianScore = request.json.get('medianScore')

    db.session.commit()

    return album_schema.jsonify(album)

@albumsBP.route('/delete/<albumID>', methods=["DELETE"])
def delete_album(albumID):
    album = Album.query.filter_by(albumID=albumID).one_or_none()

    if not album:
        return jsonify({'error': 'Album not found'}), 404

    db.session.delete(album)
    db.session.commit()

    return album_schema.jsonify(album)

