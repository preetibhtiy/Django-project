from django.contrib import admin
from .models import Employee

# Register your models here.
class Employeedata(admin.ModelAdmin):
    list_display=['eid','ename','econtact']
admin.site.register(Employee,Employeedata)