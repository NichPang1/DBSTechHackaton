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

app = Flask(__name__)

# db config
app.config['MYSQL_HOST'] = os.getenv("DB_HOST")
app.config['MYSQL_USER'] = os.getenv("DB_USERNAME")
app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("DB_NAME")
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' # return items as array of objects

# # flask configuration - if there is an exception hidden inside an extension of flask, progogate it into the main app (so we can see it)
# app.config["PROPAGATE_EXCEPTIONS"] = True 
# app.config["API_TITLE"] = "Stores REST API" # Title in our documentation
# app.config["API_VERSION"] = "v1" # Version of our API, we are working on
# app.config["OPENAPI_VERSION"] = "3.0.3" # A standard for API documentation, (tell flask smorest to use 3.0.3)
# app.config["OPENAPI_URL_PREFIX"] = "/" # Tell flask smorest where the root of the API is (where all our end points start)
# # Tell flask smorest to use swagger for the API documentation
# app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
# # Tell flask smorest where to load the swagger code (URL)
# app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# MySQL Database Connection
# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password@localhost/bank'

# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# secret for jwt
app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'

# set cors
CORS(app)

# load config
load_dotenv()

# setup mysql
mysql = MySQL(app)

@app.route("/hello")
def create_user():
    return 'Hello World!'

@app.route("/read", methods = ['GET'])
def read_tmp():
    # body = request.get_json()
    # tid = body['TransactionID']
    # sql_string = f'DELETE FROM bank.scheduledtransactions WHERE TransactionID = {tid}'
    sql_string = f'SELECT * FROM ScheduledTransactions'
    cursor = mysql.connection.cursor()
    results = cursor.execute(sql_string)
    if results > 0:
        rows = cursor.fetchall()
        return jsonify(rows)
    else:
        return make_response('No transaction founds', 403)
    # mysql.connection.commit()

@app.route("/deleteTransaction", methods = ['DELETE'])
def delete_transaction():
    body = request.get_json()
    tid = body['TransactionID']
    sql_string = f'DELETE FROM bank.scheduledtransactions WHERE TransactionID = {tid}'
    cursor = mysql.connection.cursor()
    results = cursor.execute(sql_string)
    mysql.connection.commit()
