from django.urls import path

from .views import (
   post_list,
   concrete_post,
   add_post,
   delete_post,
   edit_post,
)

urlpatterns = [
    path('post/add/', add_post, name='add_post'),
    path('post/edit/<int:post_id>/', edit_post, name='edit_post'),
    path('post/delete/<int:post_id>/', delete_post, name='delete_post'),
    path('post/view/<int:post_id>/', concrete_post, name='concrete_post'),
    path('', post_list, name='post_list'),
]
