release: python manage.py migrate --no-input
web: gunicorn backend.wsgi 
worker: celery -A backend worker -l INFO