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

# MySQL Database Connection
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:password@localhost/bank'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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

@app.route("/deleteTransaction")
def delete_transaction():
    body = request.get_json()
    tid = body['TransactionID']
    sql_string = f'DELETE FROM bank.scheduledtransactions WHERE TransactionID = {tid}'
    cursor = mysql.connection.cursor()
    cursor.execute(sql_string)
    mysql.connection.commit()
