from django.urls import path

from .views import access, index

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('access/', access, name='access'),
]
