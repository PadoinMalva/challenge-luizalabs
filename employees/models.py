from django.db import models
from django.core.exceptions import FieldDoesNotExist
from django.utils import timezone

class Employees(models.Model):
    class Meta:
        app_label = 'employees'
        managed = True
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    departament = models.TextField()
    createdAt = models.DateField()