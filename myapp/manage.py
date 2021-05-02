import os

from flask_migrate import MigrateCommand
from flask_assets import ManageAssets
from flask_script import Manager

from myapp import create_app

app = create_app(config=os.environ.get("APP_CONFIG"))
manager = Manager(app)
manager.add_command("db", MigrateCommand)
manager.add_command("assets", ManageAssets())

if __name__ == "__main__":
    manager.run()
