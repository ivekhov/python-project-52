### Hexlet tests and linter status:
[![Actions Status](https://github.com/ivekhov/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ivekhov/python-project-52/actions)

### Example service:

- https://python-task-manager-ru.hexlet.app/ 


### Project on Render: 
https://python-project-52-nkwi.onrender.com/

## Important resources and guidelines

- https://12factor.net/ru/ 
- https://pypi.org/project/dj-database-url/
- Project page: https://ru.hexlet.io/projects/52/members/43671
- https://ru.hexlet.io/projects/52/members/43671

## Django

- Docs: https://docs.djangoproject.com/en/5.1/ 
- https://www.djangoproject.com/start/
- https://docs.djangoproject.com/en/5.1/intro/tutorial01/ 
- Course: https://ru.hexlet.io/courses/python-django-basics 


## Project repo
- https://github.com/ivekhov/python-project-52



## Commands 

Creating project:

```bash
$ uv run django-admin startproject task_manager .
```

Starting project
```bash
$ uv run python3 manage.py runserver
```


## Render Details 

- Project Settings  https://dashboard.render.com/web/srv-cub2pj52ng1s73alm1m0/settings 

- Database instance https://dashboard.render.com/d/dpg-cub1t6bqf0us73cc3a00-a

- Render instructions

    - https://render.com/docs/deploy-django
    - https://dashboard.render.com/web/srv-cub2pj52ng1s73alm1m0/settings




## Django notes

Машрут - адреса, urls
Контроллер, обработчик - слой кода, вьюхи, views 
Шаблон - html templates 


Эта команда сработала 
```render-start:
	gunicorn task_manager.wsgi
```