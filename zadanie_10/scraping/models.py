from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    names = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.names}"

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.text}"