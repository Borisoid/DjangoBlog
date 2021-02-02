from django import forms

from .models import Post


class DeleteForm(forms.Form):
    pass

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        # fields = ('header', 'short_description', 'text', 'category',)
        exclude = ('tags', 'image',)
        labels = {
            'header': 'Header', 
            'short_description': 'Short description', 
            'text': 'Text', 
            'image': 'Image', 
            'tags': 'Tags',
            'category': 'Category',
        }
