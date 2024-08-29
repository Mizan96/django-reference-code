from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
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

    # def get_queryset(self, request):
    #     qs = super(CarAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)
    
    # def has_change_permission(self, request, obj=None):
    #     if not obj:
    #         return True
    #     return obj.user == request.user or request.user.is_superuser
    

    # def get_readonly_fields(self, request, obj):
    #     if request.user.is_superuser:
    #         return []
    #     return ['user']

    
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Owner)
admin.site.register(Passenger, CarAdmin)