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
from blocklist import BLOCKLIST
from flask_smorest import Api
from flask_jwt_extended import JWTManager
import secrets

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
# app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
app.config["JWT_SECRET_KEY"] = str(secrets.SystemRandom().getrandbits(128))
jwt = JWTManager(app)


# Checks if token is in blocklist, returns error if token is blocked
@jwt.token_in_blocklist_loader
def check_if_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST

# Error message for  blocked tokens
@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {"description": "The token has been revoked.", "error": "token_revoked"}
        ), 401
    )




# Error Messages for JWT Token

# 1. Expired Token
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({"message": "The token has expired.", "error": "token_expired"}, 401)
    )

#  2. Invalid Token
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
            {"message": "Signature verification failed.", "error": "invalid_token"}, 401)
    )

# 3. Unauthroized Token
@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {"description": "Request does not contain access token.", "error": "authorization_required"}
        )
    )

# 4. Needs Fresh Token
@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {
                "description": "The token is not fresh.",
                "error": "fresh_token_required"
            }
        ), 401
    )

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

