from django.contrib import admin

# Register your models here.
from .models import Employee, Authority, AdminView, EmployeeLogin
from django.contrib.auth.admin import UserAdmin


admin.site.register(Employee,AdminView)
admin.site.register(Authority)
admin.site.register(EmployeeLogin)