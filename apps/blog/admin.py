from django.contrib import admin

from .models import (
    Tag,
    Category,
    Post,
)


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
