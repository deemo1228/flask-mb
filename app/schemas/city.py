from marshmallow import Schema, fields, validate


class CitySchema(Schema):
    city_select = fields.Integer(required=True)
    user_name = fields.Str(validate=validate.Length(min=1))  # 字串字數最小值為1
