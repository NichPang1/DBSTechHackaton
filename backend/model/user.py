from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(20), unique=True, nullable=False)
    Password = db.Column(db.String(256), nullable=False)
    FirstName = db.Column(db.String(255), nullable=False)
    LastName = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255), nullable=False)
    OpIntoPhyStatements = db.Column(db.String(1), nullable=False)