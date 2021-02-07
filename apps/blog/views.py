from django.shortcuts import (
    render,
    redirect,
)
from django.http import Http404
from django.forms.models import model_to_dict

from .models import (
    Post,
)

from .forms import (
    DeleteForm,
    PostForm,
    SearchForm,
)


def post_list(request):
    if request.method == 'GET':

        posts = Post.objects

        if 'csrfmiddlewaretoken' in request.GET:

            search_form = SearchForm(request.GET)
            if search_form.is_valid():

                lookup = {
                    'tags': 'tags__in',
                    'header': 'header__icontains',
                    'short_description': 'short_description__icontains',
                }

                filter_dict = {
                    lookup.get(key, key): value
                    for key, value
                    in search_form.cleaned_data.items()
                    if value
                }

                posts = posts.filter(**filter_dict).distinct()

        return render(
            request, 'post_list.html',
            {'posts': posts.all(), 'form': SearchForm()}
        )

    raise Http404


def concrete_post(request, post_id: int):

    post = Post.objects.filter(id=post_id).first()
    if post:

        if request.method == 'GET':

            form = DeleteForm()
            return render(
                request, 'concrete_post.html',
                {'post': post, 'delete_form': form}
            )

    raise Http404


def delete_post(request, post_id: int):

    if request.method == 'POST':
        Post.objects.filter(id=post_id).delete()

        return redirect('post_list')

    raise Http404


def edit_post(request, post_id: int):

    post_query = Post.objects.filter(id=post_id)

    if request.method == 'GET':
        post = post_query.first()
        return render(
            request, 'post_form.html',
            {'post': post,
                'form': PostForm(model_to_dict(post, exclude='image'))}
        )

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            post = Post.m2m_from_form(form.cleaned_data, id=post_id)

            return redirect('concrete_post', post_id=post_id)

    raise Http404


def add_post(request):
    if request.method == 'GET':
        return render(request, 'post_form.html', {'form': PostForm()})

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            post = Post.m2m_from_form(form.cleaned_data)

            return redirect('concrete_post', post_id=post.id)

    raise Http404
