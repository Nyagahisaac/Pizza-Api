from flask import app
from app import create_app,db
from  app.auth.v1.models.user_models import Role, User
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand

app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(User = User, app = app, db = db, Role = Role)
if __name__ == '__main__':
    manager.run()


