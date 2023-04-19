from django.contrib import admin
import csv
from django.http import HttpResponse

from accounts.admin import export_reg
from .models import vehicle,employee,bin_color,Bins,location,Driver,complaintpost,workupdation,scheduleingday,Feed_back,product
from django.contrib.auth.models import Group
# admin.site.register(Bins)
# admin.site.register(vehicle)
# admin.site.register(employee)
admin.site.register(bin_color)
# admin.site.register(location)
# admin.site.register(Driver)
# admin.site.register(complaintpost)
# admin.site.register(workupdation)
# admin.site.register(scheduleingday)
admin.site.register(Feed_back)

def export_complaint(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Bins.csv"'
    writer = csv.writer(response)
    writer.writerow(['Location','Bin Number','Complaint'])
    registration = queryset.values_list('c_landmark','bin_number','c_complant')
    for i in registration:
        writer.writerow(i)
    return response


export_complaint.short_description = 'Export to csv'
class complaintpostAdmin(admin.ModelAdmin):
    list_display = ['c_landmark','bin_number','c_complant']
    actions = [export_reg]
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(complaintpost,complaintpostAdmin)
def export_bin(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Bins.csv"'
    writer = csv.writer(response)
    writer.writerow(['Bin Name','Bin color','Bin Address1','Bin Address2 ','Bin Address3', 'Zip code'])
    registration = queryset.values_list('Bin_name','Bin_color','Bin_address1','Bin_address2','Bin_address3','pincode')
    for i in registration:
        writer.writerow(i)
    return response


export_bin.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['Bin_name','Bin_color','Bin_address1','Bin_address2','Bin_address3','pincode']
    actions = [export_bin]
admin.site.register(Bins,RegAdmin)


def export_driver(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Driver.csv"'
    writer = csv.writer(response)
    writer.writerow(['Driver Name','Driver Address','Email ','Phone', 'Licence NO'])
    registration = queryset.values_list('driver_name','driver_address','driver_email','driver_phone','driver_licence')
    for i in registration:
        writer.writerow(i)
    return response


export_driver.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['driver_name','driver_address','driver_email','driver_phone','driver_licence']
    actions = [export_driver]
admin.site.register(Driver,RegAdmin)



def export_Day(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Day.csv"'
    writer = csv.writer(response)
    writer.writerow(['Region','Direction','Day'])
    registration = queryset.values_list('region','direction','day')
    for i in registration:
        writer.writerow(i)
    return response


export_Day.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['region','direction','day']
    actions = [export_Day]
admin.site.register(scheduleingday,RegAdmin)



def export_vehicle(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vehicle.csv"'
    writer = csv.writer(response)
    writer.writerow(['Registered No','Registered Owner','Registered Address','Makers Class', 'Vehicle Class','Engine','Insurance'])
    registration = queryset.values_list('register_no','regd_owner','reg_address','makers_class','vehicle_class','engine','insurance')
    for i in registration:
        writer.writerow(i)
    return response


export_vehicle.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['register_no','regd_owner','reg_address','makers_class','vehicle_class','engine','insurance']
    actions = [export_vehicle]
admin.site.register(vehicle,RegAdmin)

def export_employee(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="employee.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name','Address','Email','Phone'])
    registration = queryset.values_list('emp_name','emp_address','emp_email','emp_phone')
    for i in registration:
        writer.writerow(i)
    return response


export_employee.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['emp_name','emp_address','emp_email','emp_phone']
    actions = [export_employee]
admin.site.register(employee,RegAdmin)


def export_workupdation(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="workupdation.csv"'
    writer = csv.writer(response)
    writer.writerow(['Bin Name','Location','Time','Date','Status','Driver Name'])
    registration = queryset.values_list('Bin_id','Location','Time','Date','status','Driver_name')
    for i in registration:
        writer.writerow(i)
    return response


export_workupdation.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['Bin_id','Location','Time','Date','status','Driver_name']
    actions = [export_workupdation]
admin.site.register(workupdation,RegAdmin)



def export_location(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="location.csv"'
    writer = csv.writer(response)
    writer.writerow(['Location','Employee Name','Phone','Driver Name'])
    registration = queryset.values_list('region','employee_name','phone','status')
    for i in registration:
        writer.writerow(i)
    return response


export_location.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['region','employee_name','phone','status']
    actions = [export_location]
admin.site.register(location,RegAdmin)


def export_product(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="product.csv"'
    writer = csv.writer(response)
    writer.writerow(['Product Id','Product Name','Product Description','Product Price','Product Image'])
    registration = queryset.values_list('prd_id','prd_name','prd_discription','prd_price','prd_img')
    for i in registration:
        writer.writerow(i)
    return response


export_product.short_description = 'Export to csv'


class RegAdmin(admin.ModelAdmin):
    list_display = ['prd_id','prd_name','prd_discription','prd_price','prd_img']
    actions = [export_product]
admin.site.register(product,RegAdmin)



# Register your models here.
