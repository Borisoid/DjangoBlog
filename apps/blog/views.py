from django.shortcuts import render

from .models import(
    Post,
)

def post_list(request):
    raise NotImplementedError

def concrete_post(request, post_id: int):
    post = Post.objects.filter(id=post_id).first()

    if request.method == 'GET':
        return render(request, 'concrete-post.html', {'post': post})

def add_post(request):
    raise NotImplementedError
