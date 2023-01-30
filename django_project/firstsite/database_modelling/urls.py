from django.contrib import admin
from django.urls import path

from database_modelling import views


urlpatterns = [
    path("", views.RelationshipView)
]
