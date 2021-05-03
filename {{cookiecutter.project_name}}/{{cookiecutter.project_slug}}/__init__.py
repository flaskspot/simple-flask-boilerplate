from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Flask-SQLAlchemy
db = SQLAlchemy()
# Flask-Migrate
migrate = Migrate()



def create_app(config="myapp.config.ProductionConfig"):
    """Creates Flask Application

    Args:
        config (str, optional): . Defaults to "app.config.ProductionConfig".

    Returns:
        app: Returns flask app object
    """
    app = Flask(__name__)

    app.config.from_object(config)  # get configs

    # Initialize add-ons
    db.init_app(app)  # Database
    migrate.init_app(app, db)  # Flask-Migrate

    # Include All models
    from {{cookiecutter.project_slug}}.models import User

    # Import and register Blueprints
    from {{cookiecutter.project_slug}}.views.main import main

    app.register_blueprint(main)

    # import and register your blueprints here

    return app
