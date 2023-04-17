from django.contrib import admin
from django.contrib. auth.models import Group
import csv
from django.http import HttpResponse
from .models import Account
# admin.site.register(Account)
admin.site.unregister(Group)
def export_reg(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registration.csv"'
    writer = csv.writer(response)
    writer.writerow(['First Name','Last Name','Email','Phone','Address','City', 'Zip code','District','Role'])
    registration = queryset.values_list('first_name','last_name','email','contact','address','land_mark','pincode','district','role')
    for i in registration:
        writer.writerow(i)
    return response


export_reg.short_description = 'Export to csv'



class RegAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','contact','address','land_mark','pincode','district','role']
    actions = [export_reg]
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Account,RegAdmin)
# Register your models here.
