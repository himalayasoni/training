from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=50)
    employee = models.ManyToManyField(Employee)

    def __str__(self):
        return self.title
