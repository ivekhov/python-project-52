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


------------


# Django notes

Машрут - адреса, urls
Контроллер, обработчик - слой кода, вьюхи, views 
Шаблон - html templates 

В шаблоне идет обращение к переменной, которая передается в него из вьюхи / контроллера, в контроллере эта переменная явно обозначается стрингой. 
В контроллере логика работы с переменной реализуется внутри функции и эта переменная через словарь стринга: переменная передается в шаблон.
В контроллере явно называется имя шаблона, который используется и который существует в коде приложения 


Для Render com сработала 

```make
render-start:
	gunicorn task_manager.wsgi
```

Подпроекты внутри основного приложения Джанго - такие же (почти) джанго-приложения. Создаются админской утилитой джанго, лежат внутри основного 
приложения 

```bash
uv run django-admin startapp NAME
```

Шаблоны подпроектов лучше складывать (зеркалить структуру) в головную templates проекта. т е не держать шаблоны в подпроектах, а централизованно


####  Расширение шаблонов

Можно использовать столько уровней наследования, сколько необходимо. Один из распространенных способов использования наследования — трехуровневый подход:

- Создание base.html шаблона, который содержит основной внешний вид сайта
- Создание base_SECTIONNAME.html шаблонов для каждого раздела сайта, например, base_article.html, base_news.html. Эти шаблоны расширяют base.html и включают в себя стили для конкретных разделов
- Создание отдельного шаблона для каждого типа страницы, например, новостной статьи или записи в блоге. Эти шаблоны расширяют соответствующий шаблон раздела

Такой подход максимизирует повторное использование кода и помогает добавлять элементы в области общего содержимого, например, навигацию по всему разделу.



### Маршрутизация 

В urls.py:

```python
from django.urls import path, include  # <- добавлен include

from hexlet_django_blog import views

urlpatterns = [
    path('', views.index),
    path('articles/', include('hexlet_django_blog.article.urls')),  # <- новая строчка
    path('admin/', admin.site.urls),
]
```

В шаблоне переменные: 

```html
{% for user in users %}
<p>This is user {{ user.id }}</p>
{% endfor %}
```


