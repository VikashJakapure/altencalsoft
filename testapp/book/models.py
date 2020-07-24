from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Book(models.Model):
    name=models.CharField(max_length=30)
    pages=models.FloatField()
    description=models.TextField(max_length=120)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('book_app:details', args=[str(self.id)])

