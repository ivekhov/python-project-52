from django.urls import path

from task_manager.users.views import (
    IndexView,
    UserFormCreateView,
    UserFormEditView,
    UserFormDeleteView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='users'),
    path('create/', UserFormCreateView.as_view(), name='users_create'),
    path('<int:pk>/update/', UserFormEditView.as_view(), name='users_update'),
    path('<int:pk>/delete/', UserFormDeleteView.as_view(), name='users_delete'),
]
