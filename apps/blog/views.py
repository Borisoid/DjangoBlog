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
    
    post_id = request.GET.get('id')
    if post_id:

        post = Post.objects.filter(id=post_id).first()
        if post:
            
            if request.method == 'GET':
                
                form = DeleteForm()
                return render(request, 'concrete-post.html', 
                    {
                        'post': post,
                        'delete_form': form
                    }
                )
        
    raise Http404


def delete_post(request):

    post_id = request.POST.get('id')

    if post_id:

        if request.method == 'POST':
            Post.objects.filter(id=post_id).delete()
            
            return HttpResponse(f'Post id={post_id} has been deleted')

    raise Http404

def edit_post(request):

    post_id = request.GET.get('id')

    if post_id:
        post_query = Post.objects.filter(id=post_id)

        if request.method == 'GET':
            post = post_query.first()
            return render(request, 'post_form.html', 
                {'post': post, 'form': PostForm(model_to_dict(post, exclude='image'))}
            )

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():

                tags = form.cleaned_data.pop('tags')

                post = Post(**form.cleaned_data)
                post.id = post_id
                post.save()
                post.tags.set(tags)

                return HttpResponse(f'Post id={post_id} has been edited')

    raise Http404


def add_post(request):
    if request.method == 'GET':
        return render(request, 'post_form.html',
            {'form': PostForm()}
        )

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():

            tags = form.cleaned_data.pop('tags')

            post = Post(**form.cleaned_data)
            post.save()
            post.tags.set(tags)

            return HttpResponse(f'Post id = {post.id} has been created')

    raise Http404


