# laughter-reduction-api

## Quickstart

- `pipenv install`
- `pipenv shell`
- `python main.py`

## Commands

- `pipenv install Flask Flask-SQLAlchemy psycopg2-binary marshmallow gunicorn`
- `brew tap heroku/brew && brew install heroku`
- `psql postgres`
  - `CREATE DATABASE joke_api;`
  - `CREATE DATABASE joke_api_test;`
  - `\c joke_api;`
  - `\dt;`
- `python test.py -v`
- `heroku addons:create heroku-postgresql:hobby-dev --app laughter-reduction`
- `heroku config --app laughter-reduction`
- `heroku pg:psql --app laughter-reduction`
- `pip freeze > requirements.txt`
- `pip install autoenv`
