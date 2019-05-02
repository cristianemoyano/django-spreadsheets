rs:
	python manage.py runserver

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations

superuser:
	python manage.py createsuperuser