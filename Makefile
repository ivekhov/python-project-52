install:
	uv sync

start:
	uv run python3 manage.py runserver

PORT ?= 8000
stop:
	lsof -ti :$(PORT) | xargs kill -9

status:
	lsof -ti :$(PORT)

upgrade:
	uv sync --upgrade

lint:
	uv tool run ruff check .

lint_fix:
	uv tool run ruff check . --fix

migrations:
	uv run python3 manage.py migrate

render-start:
	gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

prepare_dep_fo_render:
	uv pip freeze > requirements.txt

collectstatic:
	uv run python3 manage.py collectstatic --no-input

migrate:
	uv run python3 manage.py migrate

make_migrations:
	uv run python3 manage.py makemigrations
