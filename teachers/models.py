from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    birth_data = models.DateField()
