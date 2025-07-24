from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from flask_migrate import Migrate
from flask_executor import Executor  # type: ignore
from flask_cors import CORS  # type: ignore
from loguru import logger

db: SQLAlchemy = SQLAlchemy(model_class=Model)
migrate = Migrate()
executor = Executor()


def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    executor.init_app(app)
    CORS(app)
    logger.add("logs/app.log", rotation="500 KB", enqueue=True)
