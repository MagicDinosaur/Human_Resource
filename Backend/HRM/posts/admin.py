from django.contrib import admin

# Register your models here.
from .models import Employee, Authority, AdminView



admin.site.register(Employee,AdminView)
admin.site.register(Authority)
# admin.site.register(AdminView)