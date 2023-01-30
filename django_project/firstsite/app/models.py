from django.db import models

# Create your models here.


class Player(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    team = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    batting_order = models.CharField(max_length=30)
