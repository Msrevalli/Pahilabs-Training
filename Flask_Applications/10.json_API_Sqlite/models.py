# models.py
from marshmallow import Schema, fields

class User:
    def __init__(self, username, theme, image):
        self.username = username
        self.theme = theme
        self.image = image

class UserSchema(Schema):
    username = fields.Str()
    theme = fields.Str()
    image = fields.Url()

# Sample data
users_db = [
    User(username="john_doe", theme="dark", image="http://example.com/john.jpg"),
    User(username="jane_doe", theme="light", image="http://example.com/jane.jpg"),
]
