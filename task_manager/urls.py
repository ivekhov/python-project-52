from django.contrib import admin
from django.urls import path, include

from task_manager import views

urlpatterns = [
    path('', views.index),
    path('users/', include('task_manager.users.urls'), name='users'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('admin/', admin.site.urls, name='admin'),


    # routes from task
    # path(),

]
