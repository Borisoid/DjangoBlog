from django.shortcuts import render
from django.http import Http404, HttpResponse

from .models import(
    Post,
)



def post_list(request):
    raise NotImplementedError

def concrete_post(request):
    
    if request.method == 'GET':
        post_id = request.GET.get('id')
        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post:
                return render(request, 'concrete-post.html', 
                    {'post': post,}
                )
        
        raise Http404

def delete_post(request):
    if request.method == 'GET':
        post_id = request.GET.get('id')
        if post_id:
            Post.objects.filter(id=post_id).delete()
            
            return HttpResponse('Deleted')

    raise Http404

def add_post(request):
    raise NotImplementedError
