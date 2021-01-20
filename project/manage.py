import os
import unittest
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import (create_app, db)  # importing our app
from app import blueprint  # importing services
from app.main.models import *  # importing all our db models for migrations


app = create_app(os.getenv('FLASK_ENV') or 'dev')  # dev, prod or test
app.register_blueprint(blueprint)  # registering in Flask application instance
app.app_context().push()
# Instantiates the manager and migrate classes
# by passing the app instance to their respective
# constructors
manager = Manager(app)
migrate = Migrate(app, db)
# Exposing all the database migration commands
# through Flask-Script
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0', port=5000)  # host exposed (works with docker)


@manager.command
def test():
    """Runs the unit tests"""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def postal_codes():
    """Run PostalCodes sql file to migrate data un postal_codes table
    THIS WORKS ONLY ON A POSTGRES DB
    """
    print('Deleting previous postal_codes')
    db.engine.execute('DELETE FROM postal_codes;')
    db.engine.execute('ALTER SEQUENCE postal_codes_id_seq RESTART WITH 1;')
    with open('postal_codes_mex_2018-10-06.sql', 'r') as sql_file:
        print('Migrating from file...')
        result = db.engine.execute(sql_file.read())
        print('Postal Code migrated ({} rows)'.format(result.rowcount))
        return 0


if __name__ == '__main__':
    manager.run()
