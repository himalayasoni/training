from django.db import models

# Create your models here.


class Player(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    team = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    average = models.IntegerField()
    batting_order = models.CharField(max_length=30)
