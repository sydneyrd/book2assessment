from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    """The Pet Model - Add your code below this line"""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    type = models.ForeignKey("PetType", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_activity = models.CharField(max_length=250)
