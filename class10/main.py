from flask import Flask, request, jsonify
import bcrypt
import psycopg2

app = Flask(__name__)

# --- Database Setup ---
def get_db_connection():
    return psycopg2.connect(
        dbname="auth", 
        user="postgres", 
        password="hello123", 
        host="localhost"
    )

class AuthService:
    def sign_up(self, username, password):
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            # 1. Check if user exists
            cur.execute("SELECT name FROM usr WHERE name = %s", (username,))
            if cur.fetchone():
                return False, "Username already taken"

            # 2. HASH the password using bcrypt
            # bcrypt needs bytes, so we encode the string
            hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # 3. Insert user (storing the hash as a string/byte)
            cur.execute("INSERT INTO usr (name, pswd) VALUES (%s, %s)", (username, hashed_pw.decode('utf-8')))
            conn.commit()
            return True, "Account created"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            cur.close()
            conn.close()

    def login(self, username, password):
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT pswd FROM usr WHERE name = %s", (username,))
            result = cur.fetchone()
            
            if result:
                stored_hash = result[0].encode('utf-8')
                # 4. Check the provided password against the stored hash
                if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
                    return True
            return False
        finally:
            cur.close()
            conn.close()

auth_service = AuthService()

# --- Flask Routes ---

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400
    
    success, message = auth_service.sign_up(data['username'], data['password'])
    
    if success:
        return jsonify({"message": message}), 201
    return jsonify({"error": message}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    username = data.get('username')
    password = data.get('password')
    
    if auth_service.login(username, password):
        return jsonify({"message": f"Welcome back, {username}!"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
     

