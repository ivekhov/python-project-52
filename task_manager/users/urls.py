from django.urls import path

from task_manager.users.views import (
    IndexView,
    UserFormCreateView,
    UserFormEditView,
)

urlpatterns = [
    path('', IndexView.as_view()),
    path('create/', UserFormCreateView.as_view(), name='users_create'),
    path('<int:pk>/update/', UserFormEditView.as_view(), name='users_update'),
]
