from flask import request
from flask.views import MethodView # to create classes
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt

from db import db
from model.user import UserModel

from schemas import UserSchema

# Create blueprint
blp = Blueprint("users", __name__, description="Operations in users")

@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True)) # Return response, to user (client)
    # Get all users
    def get(self):
        return UserModel.query.all()
