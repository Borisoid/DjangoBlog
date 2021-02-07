from django import forms

from .models import (
    Category,
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
        widget=forms.SelectMultiple,
        required=False,
    )


class SearchForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple,
        required=False,
    )

    category = forms.ModelChoiceField(Category.objects, required=False)

    search_keywords = forms.CharField(
        max_length=300,
        required=False
    )
