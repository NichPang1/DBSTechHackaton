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

# feature 2
@app.route("/userInfo/<int:id>")
def get_all_users(id):
    cursor = mysql.connection.cursor()
    resultValue = cursor.execute('select * from bankaccount where userid = {}'.format(id))
    if resultValue > 0:
        rows = cursor.fetchall()
        return jsonify(rows)
    else:
        return make_response('There are no user found.',  402)

# feature 3
@app.route("/transactions/<int:id>")
def get_user(id):
    cursor = mysql.connection.cursor()
    resultValue = cursor.execute('select * from scheduledtransactions inner join (SELECT distinct(bankaccount.AccountID) FROM user INNER JOIN bankaccount ON user.userid = bankaccount.userid where user.userid = {}) as a on scheduledtransactions.AccountID = a.accountid'.format(id))
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
        return make_response('User updated successfully', 200)
    except Exception:
        return 'Failed to update user'
