from django.shortcuts import (
    render,
    redirect,
)
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from .forms import LoginForm


def custom_login(request):
    if request.user.is_authenticated:
        redirect('post_list')

    if request.method == 'GET':
        return render(request, 'login.html', {'form': LoginForm()})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)

                return redirect('post_list')

        return render(request, 'login.html',
                      {'is_invalid': True, 'form': form})


def custom_logout(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('user_login')
