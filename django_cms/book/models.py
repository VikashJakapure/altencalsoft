from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Book(models.Model):
    bid=models.IntegerField()
    bname=models.CharField(max_length=30)
    bpages=models.FloatField()
    def __str__(self):
        return self.sname