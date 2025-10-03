# Ex02 Django ORM Web Application
## Date:03/10/25

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

Models.py
from django.db import models
from django.contrib import admin

class Employee(models.Model):
    car_brand = models.CharField(max_length=20, help_text="Employee ID")
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    release year = models.IntegerField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('car_brand','model','price','release year')
admin.py
from Django.contrib import admin
from .models import Employee,EmployeeAdmin
admin.site.register(Employee, EmployeeAdmin)



## OUTPUT


<img width="1919" height="1079" alt="Screenshot 2025-10-03 092318" src="https://github.com/user-attachments/assets/34fda676-216f-42f4-b11d-da77c4984755" />

<img width="1919" height="1079" alt="Screenshot 2025-10-03 092623" src="https://github.com/user-attachments/assets/30b99217-6e9e-4f12-95e1-5a9f8f487113" />

## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
