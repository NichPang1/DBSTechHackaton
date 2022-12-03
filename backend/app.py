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
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password@localhost/bank'



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








# feature 2
@app.route("/userInfo/<int:id>")
def get_all_users(id):
    cursor = mysql.connection.cursor()
    resultValue = cursor.execute('select * from bankaccount where userid = {}'.format(id))
    if resultValue > 0:
        rows = cursor.fetchall()
        return jsonify(rows)
    else:
        return make_response('There are no transactions found.',  403)

# feature 3
@app.route("/transactions/<int:id>")
def get_user(id):
    cursor = mysql.connection.cursor()
    resultValue = cursor.execute('select * from scheduledtransactions inner join (SELECT distinct(bankaccount.AccountID) FROM users INNER JOIN bankaccount ON users.userid = bankaccount.userid where users.userid = {}) as a on scheduledtransactions.AccountID = a.accountid'.format(id))
    if resultValue > 0:
        rows = cursor.fetchall()
        return jsonify(rows)
    else:
        return make_response('There are no transactions found.',  403)

# feature 4
@app.route("/insertTransaction", methods=["POST"])
def insert_transaction():
    body = request.get_json()
    try:
        check_cursor = mysql.connection.cursor()
        check_statement = 'SELECT * FROM ScheduledTransactions WHERE TransactionID = %s AND AccountID = %s'
        check_val = (body['TransactionID'], body['AccountID'])
        result = check_cursor.execute(check_statement, check_val)

        if result:
            return "Transaction already exists"
        insertion_cursor = mysql.connection.cursor()
        insertion_cursor.execute('INSERT INTO ScheduledTransactions VALUES ({}, {}, {}, "{}", {}, "{}")'.format(body['TransactionID'], body['AccountID'], body['ReceivingAccountID'], body['Date'], body['TransactionAmount'], body['Comment']))
        mysql.connection.commit()
    except Exception as e:
        return e
    return make_response('Transaction inserted successfully', 200)

# feature 5
@app.route("/deleteTransaction", methods = ['DELETE'])
def delete_transaction():
    body = request.get_json()
    cursor = mysql.connection.cursor()
    tid = body['TransactionID']
    get_string = f'SELECT * FROM ScheduledTransactions WHERE TransactionID = {tid}'
    results = cursor.execute(get_string)
    if (results <= 0):
        # Transaction not found.
        return make_response('message: Unable to find transaction', 404)
    
    del_string = f'DELETE FROM ScheduledTransactions WHERE TransactionID = {tid}'
    
    try:
        results = cursor.execute(del_string)
        mysql.connection.commit()
    except:
        return make_response('message: Failed to delete transaction', 400)
    return make_response('message: Transaction Deleted', 200)

# feature 6
@app.route("/userDetails", methods=['PUT'])
def update_user():
    try:
        params = request.args
        cursor = mysql.connection.cursor()
        resultValue = cursor.execute('select * from users where userId = {}'.format(params.get('userId')))
        if resultValue == 0:
            return make_response('User not found',  403)
        userDetails = cursor.fetchall()
        if userDetails[0]['Email'] ==  params.get('email'):
            return make_response('Email is the same!',  403)
        if userDetails[0]['Address'] ==  params.get('address'):
            return make_response('Address is the same!',  403)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE users SET `email` = '{}', `address` = '{}' WHERE `userid` = '{}'".format(
            params.get('email'), params.get('address'), params.get('userId')))
        mysql.connection.commit()
        return make_response('User updated successfully', 200)
    except Exception:
        return 'Failed to update user'

