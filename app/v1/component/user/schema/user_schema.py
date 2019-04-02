from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    user_id = fields.Integer(required=True)
    username = fields.String(required=True)
    # password = fields.String()
    role = fields.String(required=True)
    balance = fields.Integer(required=True)
    name = fields.String(required=True)
    picture = fields.String()
    phone = fields.String(validate=validate.Length(min=9, max=10))
    email = fields.Email()


