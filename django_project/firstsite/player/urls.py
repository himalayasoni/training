from django.contrib import admin
from django.urls import path
from player import views

urlpatterns = [
    path('data/', views.PlayerDataView)
]
