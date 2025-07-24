from flask import Flask
from src.app.config import Config
from src.app.extensions import init_extensions
from src.app.api.routes import api_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_extensions(app)

    app.register_blueprint(api_bp)
    return app
