from flask import Flask
from .config import Config
from .database import mongo
from .routes.usuarios import usuarios_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    mongo.init_app(app)
    app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
    return app