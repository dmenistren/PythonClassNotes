"""
Handles routing, request logic and configuration
"""
# Module imports
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import bcrypt
from jose import jwt

# Local imports
from database import db
from models import User

app = Flask(__name__)

# --- Configuration ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:toor@localhost/pythonclass'
app.config['SECRET_KEY'] = 'your_super_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# --- JWT Helper ---
def create_access_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

# --- Routes ---
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    # Validate input
    if not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({"error": "Missing fields"}), 400

    # Check existence
    if User.query.filter((User.name == data['username']) | (User.email == data['email'])).first():
        return jsonify({"error": "User or Email already exists"}), 400
    
    # Hash password
    hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    
    new_user = User(
        name=data['username'], 
        email=data['email'], 
        pswd=hashed.decode('utf-8')
    )
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Account created"}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(name=data.get('username')).first()
    
    if user and bcrypt.checkpw(data.get('password').encode('utf-8'), user.pswd.encode('utf-8')):
        # Return JWT token using user_id as requested
        token = create_access_token(user.id)
        return jsonify({
            "token": token,
            "message": f"Welcome back, {user.name}!"
        }), 200
    
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json()
    # Expected fields: email, old_pass, new_pass
    user = User.query.filter_by(email=data.get('email')).first()
    
    if not user:
        return jsonify({"error": "User not found"}), 404
        
    # Verify old password
    if not bcrypt.checkpw(data.get('old_pass').encode('utf-8'), user.pswd.encode('utf-8')):
        return jsonify({"error": "Incorrect old password"}), 401
    
    # Hash and update new password
    new_hashed = bcrypt.hashpw(data.get('new_pass').encode('utf-8'), bcrypt.gensalt())
    user.pswd = new_hashed.decode('utf-8')
    db.session.commit()
    
    return jsonify({"message": "Password updated successfully"}), 200


with app.app_context():
    db.create_all()

# if __name__ == "__main__":
#    # Create tables
#     app.run(debug=True)
