from django.contrib.auth import authenticate, login
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return HttpResponseRedirect('/orders/')

    return HttpResponseRedirect('/access/')


def access(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if 'signin' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return HttpResponseRedirect('/orders/')

    return render(request, 'users/access.html')
