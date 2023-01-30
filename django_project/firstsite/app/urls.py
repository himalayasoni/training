from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from app import views


urlpatterns = [
    path("player", csrf_exempt(views.PlayerView.as_view())),
    path("player/<int:pk>", csrf_exempt(views.PlayerParamView.as_view())),
    path("about", views.about, name='app'),
    path("", views.index, name='index')
]
