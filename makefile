rs:
	python manage.py runserver

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

superuser:
	python manage.py createsuperuser

setup:
	pip install -r requirements.txt

h-migrations:
	heroku run python3 manage.py makemigrations

h-migrate:
	heroku run python3 manage.py migrate

h-superuser:
	heroku run python3 manage.py createsuperuser

h-logs:
	heroku logs --tail

deploy:
	git push heroku master