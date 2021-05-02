from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle

# Flask-SQLAlchemy
db = SQLAlchemy()
# Flask-Migrate
migrate = Migrate()

# Flask-Assets
assets = Environment()


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
    assets.init_app(app)  # Flask-Assets

    # Register Assets
    css = Bundle("src/css/tailwind.css", filters="postcss", output="dist/css/app.css")
    assets.register("css", css)

    js = Bundle("src/js/*.js", output="dist/js/app.js")
    assets.register("js", js)

    # Include All models
    from {{cookiecutter.project_slug}}.models import User

    # Import and register Blueprints
    from {{cookiecutter.project_slug}}.views.main import main

    app.register_blueprint(main)

    # import and register your blueprints here

    return app
