from django.db import models
from django.contrib import admin

class Employee(models.Model):
    car_brand = models.CharField(max_length=20, help_text="Enter the car brand")
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    released_year = models.IntegerField()


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('car_brand', 'model', 'price', 'released_year')
