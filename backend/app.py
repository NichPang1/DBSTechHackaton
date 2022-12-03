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
# return items as array of objects
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

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
        params = request.args
        cursor = mysql.connection.cursor()
        resultValue = cursor.execute('select * from user where userId = {}'.format(params.get('userId')))
        if resultValue == 0:
            return make_response('User not found',  403)
        userDetails = cursor.fetchall()
        if userDetails[0]['Email'] ==  params.get('email'):
            return make_response('Email is the same!',  403)
        if userDetails[0]['Address'] ==  params.get('address'):
            return make_response('Address is the same!',  403)
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE user SET `email` = '{}', `address` = '{}' WHERE `userid` = '{}'".format(
            params.get('email'), params.get('address'), params.get('userId')))
        mysql.connection.commit()
        # resultValue = cursor.execute('select * from user')
        # if resultValue > 0:
        #     userDetails = cursor.fetchall()
        #     return jsonify(userDetails)
        return make_response('User updated successfully', 200)
    except Exception:
        return 'Failed to update user'
