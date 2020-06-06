from marshmallow import Schema, fields
from marshmallow.validate import Length


class JokeSchema(Schema):
    class Meta:
        fields = ("id", "joke")


class ParamsJokeSchema(Schema):
    joke = fields.Str(required=True, validate=Length(max=300))


joke_schema = JokeSchema()
jokes_schema = JokeSchema(many=True)

params_joke_schema = ParamsJokeSchema()
