from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model): 
    """
    ForeignKey = ManyToOneField()   
    Many User have nay car, but a car only have 1 user
    """
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    car     = models.CharField(max_length=120)

    def __str__(self):
        return self.car
