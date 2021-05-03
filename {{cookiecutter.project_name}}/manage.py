import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from {{cookiecutter.project_slug}} import create_app

app = create_app(config=os.environ.get("APP_CONFIG"))
manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()
