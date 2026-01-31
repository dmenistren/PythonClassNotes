from db import Session
from sqlalchemy.orm import Session as typeSession
from flask import Blueprint, request, jsonify
from model import User
from password_hash import decode_secret

login_blueprint = Blueprint("login", __name__, url_prefix='/auth')


@login_blueprint.route('/login', methods=['POST'])
def login():
    payload = request.json
    email = payload['email']
    password = payload['password']
    print(payload)
    db: typeSession = Session()
    check_user = db.query(User).filter(
        User.email == email
    ).first()
    if check_user is None:
        return jsonify({
            "msg": "user not exist"
        }), 401

    check = decode_secret(password, check_user.password)
    if check:
        return jsonify({
            "msg": "user is valid"
        })

    return jsonify({
        "msg": "password is not correct"
    })
