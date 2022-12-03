from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import datetime
import jwt
from dotenv import load_dotenv
import os
from flask_mysqldb import MySQL
from markupsafe import escape
from functools import wraps

app = Flask(__name__)

# db config
app.config['MYSQL_HOST'] = os.getenv("DB_HOST")
app.config['MYSQL_USER'] = os.getenv("DB_USERNAME")
app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("DB_NAME")
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' # return items as array of objects

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


# feature 6
@app.route("/userDetails", methods=['PUT'])
def update_user():
    try:
        body = request.get_json()
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE user SET `email` = '{}', `address` = '{}' WHERE `userid` = '{}'".format(
            body['email'], body['address'], body['userId']))
        mysql.connection.commit()
        return 'User updated successfully'
    except Exception:
        return 'Failed to update user'