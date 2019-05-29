from marshmallow import Schema, fields, validate


class MillionaireSchema(Schema):
    username = fields.String(required=True)
    name = fields.String(required=True)
    balance = fields.Integer(required=True)

