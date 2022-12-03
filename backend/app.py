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

# feature 3
@app.route("/transactions/<int:id>")
def get_all_users(id):
    cursor = mysql.connection.cursor()
    resultValue = cursor.execute('select * from scheduledtransactions inner join (SELECT distinct(bankaccount.AccountID) FROM user INNER JOIN bankaccount ON user.userid = bankaccount.userid where user.userid = {}) as a on scheduledtransactions.AccountID = a.accountid'.format(id))
    if resultValue > 0:
        rows = cursor.fetchall()
        return jsonify(rows)
    else:
        return make_response('There are no transactions found.',  403)