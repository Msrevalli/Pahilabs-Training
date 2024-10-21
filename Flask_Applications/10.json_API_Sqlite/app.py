# app.py
from flask import Flask, jsonify
from models import UserSchema, users_db

app = Flask(__name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route("/me", methods=["GET"])
def me_api():
    user = users_db[0]  # For demonstration, return the first user
    return user_schema.dump(user)

@app.route("/users", methods=["GET"])
def users_api():
    return users_schema.dump(users_db)

if __name__ == "__main__":
    app.run(debug=True)
