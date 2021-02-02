from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.forms.models import model_to_dict

from .models import(
    Post,
)

from .forms import(
    DeleteForm,
    PostForm,
)


def post_list(request):
    raise NotImplementedError

def concrete_post(request):
    
    if request.method == 'GET':
        post_id = request.GET.get('id')
        if post_id:
            post = Post.objects.filter(id=post_id).first()
            form = DeleteForm()
            if post:
                return render(request, 'concrete-post.html', 
                    {
                        'post': post,
                        'delete_form': form
                    }
                )
        
    raise Http404


def delete_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('id')
        if post_id:
            Post.objects.filter(id=post_id).delete()
            
            return HttpResponse(f'Post id={post_id} has been deleted')

    raise Http404

def edit_post(request):

    if request.method == 'GET':
        post_id = request.GET.get('id')
        if post_id:
            post = Post.objects.filter(id=post_id).first()
            return render(request, 'edit_post.html', 
                {'post': post, 'edit_form': PostForm(model_to_dict(post))}
            )

    if request.method == 'POST':
        post_id = request.POST.get('id')
        if post_id:
            post = Post.objects.filter(id=post_id)
            form = PostForm(request.POST)
            if form.is_valid():
                post.update(**form.cleaned_data)

    raise Http404


def add_post(request):
    raise NotImplementedError
