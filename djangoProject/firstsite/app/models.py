from django.db import models
from rest_framework import serializers

# Create your models here.
class Employee (models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
    
class EmployeeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields= "__all__" 