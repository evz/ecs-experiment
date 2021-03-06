from pytz import timezone

TIME_ZONE = timezone('America/Chicago')
DEFAULT_USER = {
    'name': 'eric',
    'email': 'eric@eric.com',
    'password': 'really-secret',
}

DB_USER = 'person_list'
DB_PW = 'person_list'
DB_HOST = 'database'
DB_PORT = '5432'
DB_NAME = 'person_list'

DB_CONN='postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'\
        .format(DB_USER, DB_PW, DB_HOST, DB_PORT, DB_NAME)

SECRET_KEY = 'super secret key'

# Suppress warning about memory overhead since we're not using this feature anyways
# https://github.com/mitsuhiko/flask-sqlalchemy/blob/d71afea650e0186348d81f02cca5181ed7c466e9/flask_sqlalchemy/__init__.py#L837
SQLALCHEMY_TRACK_MODIFICATIONS = False
