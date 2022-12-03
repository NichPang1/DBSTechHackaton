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

@app.route("/insert", methods=["POST"])
def insert_transaction():
    body = request.get_json()
    # try:
    #     check_cursor = mysql.connection.cursor()
    #     check_statement = 'SELECT * FROM ScheduledTransactions WHERE TransactionID = %s AND AccountID = %s'
    #     check_val = (body['TransactionID'], body['AccountID'])
    #     result = check_cursor.execute(check_statement, check_val)

    #     if result:
    #         return "Transaction already exists"
        

    insertion_cursor = mysql.connection.cursor()
    
    sqlstatement = 'INSERT INTO ScheduledTransactions VALUES (%s, %s, %s, %s, %s, %s)'
    val = (body['TransactionID'], body['AccountID'], body['ReceivingAccountID'], body['Date'], body['TransactionAmount'], body['Comment'])
    result = insertion_cursor.execute(sqlstatement, val)
    # except Exception as e:
    #     return e
    
    return result
    