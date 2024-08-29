from typing import Any
from django.contrib import admin
from    .models import Car, Driver, Owner, Passenger


# Register your models here.

class CarAdmin(admin.ModelAdmin): # adding search option into admin panel
    search_fields = ['user__username', 'user__email', 'name']
    raw_id_fields = ['user']
    readonly_fields = ['updated_by']
    class Meta:
        model = Car

    def save_model(self, request, obj, form, change):
        if not change:
            '''
            Update by user field is added
            '''
        #     obj.user = request.user
        # else:
            obj.updated_by = request.user
        obj.save()

    
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Owner)
admin.site.register(Passenger, CarAdmin)