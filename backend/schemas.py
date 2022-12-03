from marshmallow import Schema, fields

class UserSchema(Schema):
    UserID = fields.Int(dump_only=True)
    Username = fields.Str(required=True)
    Password = fields.Str(required=True)
    FirstName = fields.Str(required=False)
    LastName = fields.Str(required=False)
    Email = fields.Str(required=False)
    Address = fields.Str(required=False)
    OpIntoPhyStatements = fields.Str(required=False)

