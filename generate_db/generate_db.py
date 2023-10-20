# Description: This file is used to generate the database and populate it with data.    
# generate_db.py

 
from config import app, db
from models import User, Album  
from data import USERS, ALBUMS

def generate_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        for user in USERS:
            new_user = User()
            new_user.userID = user.get("userID")
            new_user.serverID = user.get("serverID")
            new_user.username = user.get("username")
            new_user.password = user.get("password")
            new_user.email = user.get("email")
            new_user.avatar = user.get("avatar")
            db.session.add(new_user)
        db.session.commit()

        for album in ALBUMS:
            new_album = Album()
            new_album.albumID = album.get("albumID")
            new_album.artist = album.get("artist")
            new_album.album = album.get("album")
            new_album.albumImage = album.get("albumImage")
            new_album.medianScore = album.get("medianScore")
            db.session.add(new_album)
        db.session.commit()