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
    return make_response('message: Transaction Deleted', 204)
     
