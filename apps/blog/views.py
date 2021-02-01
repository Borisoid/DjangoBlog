from django.shortcuts import render

def post_list(request):
    raise NotImplementedError

def concrete_post(request, post_id: int):
    raise NotImplementedError

def add_post(request):
    raise NotImplementedError
