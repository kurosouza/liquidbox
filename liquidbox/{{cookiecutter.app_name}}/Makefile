test:
	PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 pytest -v

run:
	PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 FLASK_APP={{cookiecutter.app_name}}.adapters.http.endpoints.py FLASK_ENV=development pipenv run flask run
	
