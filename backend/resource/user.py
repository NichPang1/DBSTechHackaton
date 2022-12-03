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

# Get all users function
@blp.route("/user")
class UserList(MethodView):
    @blp.response(200, UserSchema(many=True)) # Return response, to user (client)
    # Get all users
    def get(self):
        return UserModel.query.all()

# Register function
@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    # Register user
    def post(self, user_data):
        if UserModel.query.filter(UserModel.Username == user_data["Username"]).first():
            abort(409, message="A user with that username already exists.")

        user = UserModel(
            Username = user_data["Username"],
            Password = pbkdf2_sha256.hash(user_data["Password"]),
            FirstName = user_data["FirstName"],
            LastName = user_data["LastName"],
            Email = user_data["Email"],
            Address = user_data["Address"],
            OpIntoPhyStatements = user_data["OpIntoPhyStatements"]
        )

        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201

# Login function
@blp.route("/login")
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    # User login
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.Username == user_data["Username"]).first()
        
        # Verifies user exist and password is valid
        if user and pbkdf2_sha256.verify(user_data["Password"], user.Password):
            access_token = create_access_token(identity=user.UserID, fresh=True)
            refresh_token = create_refresh_token(identity=user.UserID)
            return {"access_token": access_token, "refresh_token": refresh_token}

        abort(401, message="Invalid credentials")
