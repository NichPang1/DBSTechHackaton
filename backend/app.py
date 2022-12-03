from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import datetime
import jwt
from dotenv import load_dotenv
import os
from flask_mysqldb import MySQL
from markupsafe import escape
from functools import wraps
from db import db
from flask_smorest import Api

from resource.user import blp as UserBlueprint

app = Flask(__name__)

# flask configuration - if there is an exception hidden inside an extension of flask, progogate it into the main app (so we can see it)
app.config["PROPAGATE_EXCEPTIONS"] = True 
app.config["API_TITLE"] = "Stores REST API" # Title in our documentation
app.config["API_VERSION"] = "v1" # Version of our API, we are working on
app.config["OPENAPI_VERSION"] = "3.0.3" # A standard for API documentation, (tell flask smorest to use 3.0.3)
app.config["OPENAPI_URL_PREFIX"] = "/" # Tell flask smorest where the root of the API is (where all our end points start)
# Tell flask smorest to use swagger for the API documentation
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
# Tell flask smorest where to load the swagger code (URL)
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# db config
app.config['MYSQL_HOST'] = os.getenv("DB_HOST")
app.config['MYSQL_USER'] = os.getenv("DB_USERNAME")
app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("DB_NAME")
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' # return items as array of objects

# MySQL Database Connection
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password@localhost/SEED_TEAM_9'



app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # Initialises flask alchemy exteinsion - allow it to connect flask app to sqlAlchemy

# secret for jwt
app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'

# set cors
CORS(app)

# load config
load_dotenv()

# setup mysql
mysql = MySQL(app)

# create tables (for user)
@app.before_first_request
def create_tables():
    db.create_all()

# Connects flask_smorest extension to the flask app
api = Api(app)

api.register_blueprint(UserBlueprint)

@app.route("/hello")
def create_user():
    return 'Hello World!'

