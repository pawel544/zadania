from django.db import models

# Create your models here.

class Author(models.Model):
    name= models.CharField(max_length=50, null=False, unique=False)

    def __str__(self):
        return f"{self.name}"
class Quate(models.Model):
    form_quate=models.CharField(max_length=100, null=False, unique=True)
    data=models.DateField(auto_now_add=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quates')

    def __str__(self):
        return f'{self.form_quate}'
