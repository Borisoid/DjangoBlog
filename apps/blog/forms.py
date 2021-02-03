from django import forms

from .models import(
    Post,
    Tag,
)


class DeleteForm(forms.Form):
    pass

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'header': 'Header', 
            'short_description': 'Short description', 
            'text': 'Text', 
            'image': 'Image', 
            'tags': 'Tags',
            'category': 'Category',
        }

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
