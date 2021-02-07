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
        blank=True,
    )


class SearchForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    category = forms.ModelChoiceField(Category.objects, required=False)

    header = forms.CharField(
        max_length=Post._meta.get_field('header').max_length,
        required=False
    )

    short_description = forms.CharField(
        max_length=Post._meta.get_field('short_description').max_length,
        required=False
    )
