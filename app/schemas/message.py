from marshmallow import Schema, fields, validate


class MessageSchema(Schema):
    user_id = fields.Integer(required=True)
    title = fields.Str(validate=validate.Length(min=1))  # 字串字數最小值為1
    content = fields.Str(validate=validate.Length(min=1))  # 字串字數最小值為1

class UpdateSchema(Schema):
    id = fields.Integer(required=True)
    current_title = fields.Str(validate=validate.Length(min=1))  # 字串字數最小值為1
    current_content = fields.Str(validate=validate.Length(min=1))  # 字串字數最小值為1