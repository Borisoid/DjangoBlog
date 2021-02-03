from django.urls import path

from .views import (
   post_list,
   concrete_post,
   add_post,
   delete_post,
   edit_post
)

urlpatterns = [
    path('add/', add_post),
    path('post/edit/', edit_post, name='edit_post'),
    path('post/delete/', delete_post, name='delete_post'),
    path('post/', concrete_post, name='concrete_post'),
    path('', post_list),
]