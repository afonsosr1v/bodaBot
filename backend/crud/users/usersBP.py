# usersBP.py

from flask import Blueprint, request, jsonify
from config import db
from models import User, user_schema, users_schema

usersBP = Blueprint('usersBP', __name__, url_prefix="/users")

@usersBP.route('/create', methods=["POST"])
def create_user():
    if not request.json:
        return jsonify({'error': 'No JSON payload received'}), 400

    userID = request.json.get('userID')
    serverID = request.json.get('serverID')
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    avatar = request.json.get('avatar')

    if not all([userID, serverID, username, password, email, avatar]):
        return jsonify({'error': 'Missing required fields'}), 400

    new_user = User()
    new_user.userID = userID
    new_user.serverID = serverID
    new_user.username = username
    new_user.password = password
    new_user.email = email
    new_user.avatar = avatar

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@usersBP.route('/get', methods=["GET"])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@usersBP.route('/get/<userID>', methods=["GET"])
def get_user(userID):
    user = User.query.get(userID)
    return user_schema.jsonify(user)

@usersBP.route('/update/<userID>', methods=["PUT"])
def update_user(userID):
    user = User.query.filter_by(userID=userID).one_or_none()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    if request.json is not None:
        user.userID = request.json.get('userID')
        user.serverID = request.json.get('serverID')
        user.username = request.json.get('username')
        user.password = request.json.get('password')
        user.email = request.json.get('email')
        user.avatar = request.json.get('avatar')

    db.session.commit()

    return user_schema.jsonify(user)

@usersBP.route('/delete/<userID>', methods=["DELETE"])
def delete_user(userID):
    user = User.query.filter_by(userID=userID).one_or_none()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)