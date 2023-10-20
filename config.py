import pathlib
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bootstrap import Bootstrap5

basedir = pathlib.Path(__file__).parent.resolve() 

app = Flask(__name__, template_folder='frontend', static_folder='frontend/static')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir / 'bodaDB.db'}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bs = Bootstrap5(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)