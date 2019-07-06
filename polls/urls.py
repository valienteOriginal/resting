from django.urls import path

from . import views

urlpatterns = [
    path('happy', views.index, name='index'),
    path('next', views.post, name='post'),
]
