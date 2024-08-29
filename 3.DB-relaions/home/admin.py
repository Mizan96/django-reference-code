from django.contrib import admin
from    .models import Car, Driver, Owner, Passenger


# Register your models here.
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Owner)
admin.site.register(Passenger)