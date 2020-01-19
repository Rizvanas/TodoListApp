# services/users/manage.py

import sys
import unittest
import coverage
from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)


COV = coverage.coverage(
    branch=True,
    include="project/*",
    omit=['project/tests/*', 'project/config.py']
)

COV.start()


@cli.command('recreate_db')
def recreate_db():
    '''Commnad recreates database'''
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('test')
def test():
    '''Command runs all tests'''
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


@cli.command('seed_db')
def seed_db():
    '''Command seeds the database'''
    User(username='rizvan', email='rizvan@mail.com').save()
    User(username='chalilovas', email='chalilovas@mail.com').save()


@cli.command()
def cov():
    '''Runs all tests and check code coverage.'''
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()
