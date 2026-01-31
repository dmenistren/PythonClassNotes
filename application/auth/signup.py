from flask import Blueprint, request, jsonify
from model import User
from password_hash import generate_secret
from db import Session
from sqlalchemy.orm import Session as typeSession

signup_app = Blueprint('signup', __name__, root_path='/auth')


@signup_app.route("/signup", methods=['POST'])
def signup():
    req_data = request.json
    db: typeSession = Session()
    user = User()
    email = req_data.get("email")
    val = db.query(User).filter(
        User.email == email,
    ).first()

    if val is not None:
        return jsonify({
            "msg": "user is already exist"
        }), 401

    user.full_name = req_data.get("full_name")
    user.email = email
    user.password = generate_secret(req_data.get("password"))
    user.Age = int(req_data.get('age', 0))

    db.add(user)
    db.commit()

    return jsonify({
        "success": "Sign up completed"
    })
