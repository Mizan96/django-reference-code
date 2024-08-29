from django.db import models
from django.contrib.auth.models import User
from django.db import models
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
    
class Driver(models.Model): 
    """
    Many to Many Relationship  
    """
    user    = models.ManyToManyField(User)
    car     = models.CharField(max_length=120)

    def __str__(self):
        return self.car
    
class Owner(models.Model): 
    """
    One to one relationship
    """
    owner   = models.OneToOneField(User,on_delete=models.CASCADE)
    car     = models.CharField(max_length=120)

    def __str__(self):
        return self.car
    

def set_delete_user():
    return User.objects.get_or_create(username='deleted')[0] # get_or_create -> (obj, true)

def limit_choices_to():
    Q = models.Q
    # return {'is_staff': True}
    return Q(username__icontains='e') #| Q(username__icontains='m')

class Passenger(models.Model):
    """
    Data base record delation
    """
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) # all the records will be deleted with user delation
    # user = models.ForeignKey(User, on_delete=models.PROTECT) # cannot delete user
    user = models.ForeignKey(User, on_delete=models.SET(set_delete_user), limit_choices_to=limit_choices_to)
    car     = models.CharField(max_length=120)

    def __str__(self):
        return self.car

