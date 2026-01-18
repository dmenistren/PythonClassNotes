from db import BaseClass, Session, Engine
from flask import Flask, jsonify, request
import model
from password_hash import generate_secret


def create_app() -> Flask:
    app = Flask(__name__)
    BaseClass.metadata.create_all(Engine)
    return app


app = create_app()


@app.route("/")
def health_check():
    return jsonify({
        "status": "Running"
    })


# Signup
@app.route("/signup", methods=['POST'])
def signup():
    req_data = request.json
    db = Session()
    user = model.User()

    user.full_name = req_data.get("full_name")
    user.email = req_data.get("email")
    user.password = generate_secret(req_data.get("password"))
    user.Age = int(req_data.get('age', 0))

    db.add(user)
    db.commit()

    return jsonify({
        "success": "Sign up completed"
    })


if __name__ == "__main__":
    app.run()
