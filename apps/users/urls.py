from django.urls import path

from .views import access, index, signout

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('access/', access, name='access'),
    path('signout/', signout, name='signout'),
]
