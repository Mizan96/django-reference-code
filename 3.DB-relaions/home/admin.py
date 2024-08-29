from django.contrib import admin
from    .models import Car, Driver, Owner, Passenger


# Register your models here.

class CarAdmin(admin.ModelAdmin): # adding search option into admin panel
    search_fields = ['user__username', 'user__email', 'name']
    # raw_id_fields = ['user']
    class Meta:
        model = Car
    
admin.site.register(Car, CarAdmin)
admin.site.register(Driver)
admin.site.register(Owner)
admin.site.register(Passenger)