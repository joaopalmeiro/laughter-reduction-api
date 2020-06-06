# laughter-reduction-api

## Quickstart

- `source env/bin/activate`
- `python main.py`

## Commands

- `python3 -m venv env`
- `pip install Flask Flask-SQLAlchemy psycopg2-binary`
- `pip install -U marshmallow`
- `psql postgres`
  - `CREATE DATABASE joke_api;`
  - `CREATE DATABASE joke_api_test;`
  - `\c joke_api;`
  - `\dt;`
- `python test.py -v`
