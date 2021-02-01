from django.contrib import admin
from django.urls import path

from .views import (
   post_list,
   concrete_post,
   add_post,
)

urlpatterns = [
    path('add/', add_post),
    path('<int:post_id>/', concrete_post),
    path('', post_list),
]