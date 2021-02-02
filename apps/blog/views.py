from django.shortcuts import render
from django.http import Http404, HttpResponse

from .models import(
    Post,
)

from .forms import(
    DeleteForm,
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

def add_post(request):
    raise NotImplementedError
