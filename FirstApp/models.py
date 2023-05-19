from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    id = models.CharField(max_length=100, primary_key=True)
    contact = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} {self.name}'
    