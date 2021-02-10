from django.urls import path
from django.conf.urls import url  # noqa
from .views import (
    custom_login,
    custom_logout,
    log_in_out,
)

urlpatterns = [
    path('login/', custom_login, name='user_login'),
    path('logout/', custom_logout, name='user_logout'),
    path('log-in-out/', log_in_out, name='user_log_in_out')
]
