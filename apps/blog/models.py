from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    header = models.CharField(max_length=50, null=False, blank=False)

    short_description = models.CharField(
        max_length=150, null=False, blank=False)

    text = models.TextField(null=False, blank=False)

    image = models.ImageField(
        upload_to='static/uploaded_images', null=True, blank=True)

    tags = models.ManyToManyField(to=Tag)

    category = models.ForeignKey(
        to=Category, default=None, on_delete=models.CASCADE)

    def __str__(self):
        tag_names = ', '.join(list(
            map(lambda tag: tag.name,
                Post.objects.filter(id=self.id).first().tags.all())
        ))
        return f'''Header - {self.header}
            | Short description - {self.short_description}
            | Category - {self.category}
            | Tags - {tag_names}'''
