# church/models.py
from django.db import models

from bootstrap_themes import list_themes
# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length=200, blank=False)

    surname = models.CharField(max_length=200, blank=False)

    age = models.IntegerField(blank=False)

    position = models.CharField(max_length=200, blank=True)

    address = models.CharField(max_length=500, blank=False)

    theme = models.CharField(max_length=255, default='default', 
            choices=list_themes())

    def __str__(self):
        
        return "{1}, {0}".format(self.name, self.surname)
