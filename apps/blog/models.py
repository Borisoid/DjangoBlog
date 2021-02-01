from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

class Post(models.Model):
    header = models.CharField(max_length=50, null=False, blank=False)
    short_description = models.CharField(max_length=150, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='static/uploaded_images')

    tags = models.ManyToManyField(to=Tag, blank=True)
    category = models.ForeignKey(to=Category, default=None, on_delete=models.CASCADE)
