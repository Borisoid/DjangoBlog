from django.contrib.auth.decorators import (
    login_required,
)
from django.core.exceptions import (  # noqa
    PermissionDenied,
)
from django.db.models import (
    Count,
    Q,
)
from django.forms.models import (
    model_to_dict,
)
from django.http import (
    Http404,
)
from django.http.response import (
    HttpResponseBadRequest,
)
from django.shortcuts import (
    redirect,
    render,
)

from .forms import (
    DeleteForm,
    PostForm,
    SearchForm,
)
from .models import (
    Post,
)


def post_list(request):
    if request.method == 'GET':

        posts = Post.objects \
                    .prefetch_related('tags') \
                    .select_related('category')

        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            filter_dict = {
                key: value
                for key, value
                in search_form.cleaned_data.items()
                if value
            }

            search_keywords = filter_dict.pop('search_keywords', None)
            if search_keywords:
                posts = posts.filter(
                    Q(header__icontains=search_keywords)
                    | Q(short_description__icontains=search_keywords)
                )

            tags = filter_dict.pop('tags', None)
            if tags:
                posts = posts \
                    .filter(tags__in=tags) \
                    .annotate(num_tags=Count('tags')) \
                    .filter(num_tags__gte=len(tags))

            posts = posts.filter(**filter_dict).distinct()

            return render(
                request, 'post_list.html',
                {'posts': posts.all(), 'form': search_form}
            )

    return HttpResponseBadRequest()


def concrete_post(request, post_id: int):

    post = Post.objects.filter(id=post_id) \
                       .prefetch_related('tags', 'category') \
                       .first()
    if post:

        if request.method == 'GET':
            form = DeleteForm()
            return render(
                request, 'concrete_post.html',
                {'post': post, 'delete_form': form}
            )

        return HttpResponseBadRequest()

    raise Http404


@login_required()
def delete_post(request, post_id: int):

    if request.method == 'POST':
        Post.objects.filter(id=post_id).delete()

        return redirect('post_list')

    raise Http404


@login_required()
def edit_post(request, post_id: int):

    post = Post.objects.filter(id=post_id) \
                       .prefetch_related('tags', 'category') \
                       .first()
    if post:

        if request.method == 'GET':
            return render(
                request, 'post_form.html',
                {'post': post,
                 'post_form': PostForm(model_to_dict(post))}
            )

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()

                return redirect('concrete_post', post_id=post_id)

        return HttpResponseBadRequest()

    raise Http404


@login_required
def add_post(request):

    if request.method == 'GET':
        return render(request, 'post_form.html', {'post_form': PostForm()})

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()

            return redirect('concrete_post', post_id=post.id)

    return HttpResponseBadRequest()
