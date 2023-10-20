# frontendBP.py is the main file for the frontend of the application.

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session

frontendBP = Blueprint('frontendBP', __name__, url_prefix="/", template_folder="templates", static_folder="static")

@frontendBP.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@frontendBP.route('/newuser', methods=["GET"])
def register():
    return render_template('addUser.html')