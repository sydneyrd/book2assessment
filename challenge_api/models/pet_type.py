from django.db import models

class PetType(models.Model):
    """PetType Model - Add your code below this line"""
    label = models.CharField(max_length=200)
