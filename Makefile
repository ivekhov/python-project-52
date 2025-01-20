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
