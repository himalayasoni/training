from django.contrib import admin
from database_modelling.models import Project, Department, Employee

# Register your models here.

admin.site.register(Project)
admin.site.register(Department)
admin.site.register(Employee)