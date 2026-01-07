from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask import jsonify

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from routes.form_routes import form_bp
from routes.response_routes import response_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)

# ✅ Allow React frontend explicitly

CORS(
    app,
    resources={r"/api/*": {"origins": "http://localhost:5173"}},
    supports_credentials=True,
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
)


app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

@jwt.unauthorized_loader
def unauthorized_callback(reason):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(reason):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token expired"}), 401


limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["100/hour"]
)

app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(form_bp, url_prefix="/api/forms")
app.register_blueprint(response_bp, url_prefix="/api/responses")

if __name__ == "__main__":
    app.run(debug=True)
