from django.contrib import admin
from django.urls import path
from app import views
from app.views import employeeListView, UserListView, employeeDetailView

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='app'),
    path("api/employee", employeeListView),
    path("api/users",UserListView),
    path("api/employee/<int:pk>", employeeDetailView)
]
