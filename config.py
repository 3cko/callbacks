import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'callbacks.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# form validation
CSRF_ENABLED = True
SECRET_KEY = 'Shibby do boo opp'
