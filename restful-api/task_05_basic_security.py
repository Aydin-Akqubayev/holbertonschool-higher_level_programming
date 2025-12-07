from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key for JWT signing
app.config['JWT_SECRET_KEY'] = 'mysecretkeydontelanyone'
jwt = JWTManager(app)

# Basic Auth users with hashed passwords
users = {
    "user1": generate_password_hash("password1"),
    "admin1": generate_password_hash("adminpass")
}

# JWT Auth users (plain text for example purposes)
jwt_users = {
    "user1": {"password": "password1", "role": "user"},
    "admin1": {"password": "adminpass", "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """Check Basic Auth credentials."""
    if username in users and check_password_hash(users[username], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Route protected with Basic Auth."""
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route('/login', methods=['POST'])
def login():
    """Login using JWT authentication."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = jwt_users.get(username)

    if not user or user.get("password") != password:
        return jsonify({"error": "Invalid credentials"}), 401

    role = user.get("role", "user")
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": role}
    )

    return jsonify({"access_token": access_token})


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Route protected with JWT."""
    return jsonify({"message": "JWT Auth: Access Granted"})


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin-only route protected with JWT."""
    current_user = get_jwt_identity()

    if current_user != "admin1":
        return jsonify({"error": "Admin access denied"}), 403

    return jsonify({"message": "Admin Access: Granted"})


if __name__ == "__main__":
    app.run(debug=True)
