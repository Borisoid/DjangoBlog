from django.urls import path
from django.conf.urls import url  # noqa
from .views import (
    custom_login,
    custom_logout,
)

urlpatterns = [
    path('login/', custom_login, name='user_login'),
    path('logout/', custom_logout, name='user_logout'),
]
