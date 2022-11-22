from django.contrib import admin

from .models import vehicle,employee,bin_color,Bins,location,Driver, complaintpost,workupdation,scheduleingday
from django.contrib.auth.models import Group
admin.site.register(Bins)
admin.site.register(vehicle)
admin.site.register(employee)
admin.site.register(bin_color)
admin.site.register(location)
admin.site.register(Driver)
admin.site.register(complaintpost)
admin.site.register(workupdation)
admin.site.register(scheduleingday)

# Register your models here.
