
from django.db import models
from location_field.models.plain import PlainLocationField
from accounts.models import Account

import datetime
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re


from django.core.validators import RegexValidator

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


class vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    register_no = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$',
                message='Register no. must be in the format XX 00 XX 0000',
                code='invalid_register_no'
            ),
        ]
    )
    regd_owner = models.CharField(max_length=100)
    reg_address = models.CharField(max_length=100)
    makers_class = models.CharField(max_length=100)
    vehicle_class = models.CharField(max_length=100)
    fuel = models.CharField(
        max_length=100,
        choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')]
    )
    engine = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Z0-9-]+$',
                message='Engine no. can only contain uppercase letters, digits, and hyphens',
                code='invalid_engine_no'
            ),
        ]
    )
    insurance = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$',
                message='Insurance no. must be in the format XX 00 XX 0000',
                code='invalid_insurance_no'
            ),
        ]
    )

    def clean(self):
        if self.insurance == self.register_no:
            raise ValidationError('Insurance no. cannot be the same as register no.')

    def __str__(self):
        return self.register_no



class employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    emp_name=models.CharField(max_length=100,default='')
    emp_address=models.CharField(max_length=200)
    emp_email=models.CharField(max_length=100, unique=True)
    emp_phone=models.BigIntegerField()
    emp_image=models.ImageField()

    def clean(self):
        if not re.match(r'^[a-zA-Z ]+$', self.emp_name):
            raise ValidationError('Employee name can only contain alphabets and spaces.')
        # Validate driver email
        if not self.emp_email:
            raise ValidationError("Email is required")
        if "@" not in self.emp_email:
            raise ValidationError("Email address is not valid")

        # Validate driver phone number
        if not self.emp_phone:
            raise ValidationError("Phone number is required")
        if len(str(self.emp_phone)) < 10 or len(str(self.emp_phone)) > 12:
            raise ValidationError("Phone number is not valid")


    def __str__(self):
            return self.emp_name


class bin_color(models.Model):
    bin_color=models.CharField(max_length=100)
    bin_type=models.CharField(max_length=100)
    def __str__(self):
            return self.bin_color


class location(models.Model):
    region = models.CharField(max_length=100)
    employee_name = models.ForeignKey(employee, verbose_name='emp_name', on_delete=models.DO_NOTHING, default="")
    phone = models.BigIntegerField()
    status = models.CharField(max_length=100)
    location1 = PlainLocationField(based_fields=['region'], zoom=7,null=True,blank=True)

    def __str__(self):
        return self.region

    def clean(self):
        super().clean()
        errors = {}

        # region field validation
        if not re.match(r'^[A-Za-z\s]+$', self.region):
            errors['region'] = 'Region field should only contain letters and spaces.'

        # phone field validation
        if not (len(str(self.phone)) == 10 and str(self.phone).isdigit()):
            errors['phone'] = 'Phone number should contain 10 digits.'

        # status field validation
        if not re.match(r'^[A-Za-z\s]+$', self.status):
            errors['status'] = 'Status field should only contain letters and spaces.'

        if errors:
            raise ValidationError(errors)

class scheduleingday(models.Model):
    region = models.ForeignKey(location,verbose_name='region',on_delete=models.DO_NOTHING,default="")
    schedule_id = models.AutoField(primary_key=True)
    direction = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    def __str__(self):
        return self.day


from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError



class Bins(models.Model):
    Bin_id = models.AutoField(primary_key=True)
    Bin_name = models.CharField(max_length=100)
    Bin_color = models.ForeignKey(bin_color, verbose_name='bin_color', on_delete=models.DO_NOTHING, default="")
    Bin_location = models.ForeignKey(location, verbose_name='region', on_delete=models.DO_NOTHING, default="")
    Bin_address1 = models.CharField(max_length=100)
    Bin_address2 = models.CharField(max_length=100)
    Bin_address3 = models.CharField(max_length=100)
    pincode = models.BigIntegerField()
    distance_KM = models.CharField(max_length=100)
    total_time = models.TimeField(default=0)
    Bin_date= models.DateField(default=0)
    Bin_status = models.CharField(max_length=50)
    collections_day = models.ForeignKey(scheduleingday,verbose_name='day',on_delete=models.DO_NOTHING,default="")
    def __str__(self):
            return self.Bin_name

class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=100)
    driver_address = models.CharField(max_length=200)
    driver_email = models.CharField(max_length=100, unique=True)
    driver_phone = models.BigIntegerField()
    driver_licence = models.CharField(max_length=100)
    driver_vehicle = models.ForeignKey(vehicle, verbose_name='register_no', on_delete=models.DO_NOTHING,default="")
    driver_location = models.ForeignKey(location, verbose_name=' region', on_delete=models.DO_NOTHING,default="")
    Allocatted_bin=models.ForeignKey(Bins,verbose_name='Bin_name',on_delete=models.DO_NOTHING,default="")
    driver_image = models.ImageField()

    def clean(self):
        if not re.match(r'^[a-zA-Z ]+$', self.driver_name):
            raise ValidationError('Driver name can only contain alphabets and spaces.')
        # Validate driver email
        if not self.driver_email:
            raise ValidationError("Email is required")
        if "@" not in self.driver_email:
            raise ValidationError("Email address is not valid")

        # Validate driver phone number
        if not self.driver_phone:
            raise ValidationError("Phone number is required")
        if len(str(self.driver_phone)) < 10 or len(str(self.driver_phone)) > 12:
            raise ValidationError("Phone number is not valid")

        # Validate driver license
        if not self.driver_licence:
            raise ValidationError("License number is required")

    def __str__(self):
        return self.driver_name


class complaintpost(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    c_landmark = models.CharField(max_length=100)
    bin_number = models.CharField(max_length=100)
    c_complant =models.CharField(max_length=500)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.c_landmark


class workupdation(models.Model):
    work_id = models.AutoField(primary_key=True)
    Bin_id = models.ForeignKey(Bins,verbose_name='Bin_name',on_delete=models.DO_NOTHING,default="")
    Location = models.ForeignKey(location,verbose_name='region',on_delete=models.DO_NOTHING,default="")
    # Area = models.ForeignKey(Bins,verbose_name='Bin_address1',on_delete=models.DO_NOTHING,default="")
    Time = models.TimeField(default=0)
    Date = models.DateField(default=0)
    status = models.CharField(max_length=100)
    Driver_name = models.ForeignKey(Driver,verbose_name='driver_name',on_delete=models.DO_NOTHING,default="")




class Feed_back(models.Model):
    feed_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    feedbacktype = models.CharField(max_length=1000,null=True)
    des_feedback = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.name


class product(models.Model):
    prd_id=models.AutoField(primary_key=True)
    prd_name=models.CharField(max_length=100,default='')
    prd_discription=models.CharField(max_length=200, unique=True)
    prd_img= models.ImageField(null=True,blank=True)
    prd_price=models.IntegerField(max_length=15)
    def __str__(self):
            return self.prd_name


class Cart(models.Model):
    products = models.ForeignKey(product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(default=1)
    price = models.IntegerField(default=0,null=True,blank=True)

    def get_product_price(self):
        price = [self.product.price]
        return sum(price)











