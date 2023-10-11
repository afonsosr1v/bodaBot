import sqlite3

conn = sqlite3.connect('bodabot.db')

reviews = [
    "id INTEGER PRIMARY KEY AUTOINCREMENT",
    "reviewID VARCHAR(255) UNIQUE NOT NULL",
    "reviewerID VARCHAR(255) NOT NULL",
    "artist VARCHAR(255) NOT NULL"
    "album VARCHAR(255) NOT NULL",
    "albumImage VARCHAR(255) NOT NULL",
    "rating INTEGER NOT NULL",
    "review VARCHAR(255) NOT NULL",
]

users = [
    "id INTEGER PRIMARY KEY AUTOINCREMENT",
    "userID VARCHAR(255) UNIQUE NOT NULL",
    "serverID VARCHAR(255) NOT NULL",
    "reviews (reviewerID) REFERENCES users(userID)"
    

        