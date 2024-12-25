from flask import Flask, jsonify
from app.extensions import db, ma, jwt, migrate
from app.models.user import User
from app.routes.user import bp as user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    @jwt.user_lookup_loader
    def user_lookup(jwt_header: dict, jwt_payload: dict):
        user_id = jwt_payload.get("sub")
        user = User.query.get(user_id) 
        
        return user
    
    @app.errorhandler(422)
    def webargs_error_handler(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code

    app.register_blueprint(user_bp)

    return app
