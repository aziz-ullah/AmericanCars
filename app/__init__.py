from flask import Flask
from app.extensions import db, ma, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    from app.routes import auth_routes
    app.register_blueprint(auth_routes)

    return app
