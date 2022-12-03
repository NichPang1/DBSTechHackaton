from marshmallow import Schema, fields

class UserSchema(Schema):
    UserID = fields.Int(dump_only=True)
    Username = fields.Str(required=True)
    Password = fields.Str(required=True)
    FirstName = fields.Str(required=True)
    LastName = fields.Str(required=True)
    Email = fields.Str(required=True)
    Address = fields.Str(required=True)
    OpIntoPhyStatements = fields.Str(required=True)

