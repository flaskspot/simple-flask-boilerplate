import os

from {{cookiecutter.project_slug}} import create_app


app = create_app(config=os.environ.get("APP_CONFIG"))


if __name__ == "__main__":
    app.run()  # run app
