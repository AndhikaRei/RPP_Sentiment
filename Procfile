web: gunicorn wsgi:app
init: flask db init --directory src/migrations
migrate: flask db migrate --directory src/migrations
upgrade: flask db upgrade --directory src/migrations