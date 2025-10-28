from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect


def index(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('orders:orders_list')

    return redirect('users:access')


def access(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if 'signin' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('orders:orders_list')

            return HttpResponseBadRequest('Invalid username or password.')
        else:
            return HttpResponseBadRequest('Invalid access method.')

    return render(request, 'users/access.html')


def signout(request: HttpRequest) -> HttpResponse:
    logout(request)

    return redirect('users:access')
