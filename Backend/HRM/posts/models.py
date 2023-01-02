from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.
#employee model
class AdminView(admin.ModelAdmin):
    readonly_fields = ('employee_joining_date',)
# lam lai  phan nay hi
class Employee(models.Model):

    # employee_id = models.AutoField(primary_key=True)
    # employee_name = models.CharField(max_length=50)
    # employee_email = models.EmailField(max_length=50, unique=True)
    # employee_phone = models.CharField(max_length=50)
    # employee_address = models.CharField(max_length=50)
    # employee_password = models.CharField(max_length=400)
    # employee_position = models.CharField(max_length= 50, choices=Position.choices)
    # employee_department = models.CharField(max_length= 50, choices=Department.choices)
    # employee_salary = models.DecimalField(max_length=50, decimal_places= 3, max_digits = 9)
    # employee_joining_date = models.DateField(auto_now_add=True, editable = True)
    # employee_leaving_date = models.CharField(max_length=50, null=True, blank=True)
    # employee_status = models.CharField(max_length=50, choices= EMPLOYEE_STATUS)
    # employee_image = models.CharField(max_length=100)
    def id(self):
        return self.employee_id
    def is_active(self):
        return self.employee_status
    is_anonymous = False
    is_authenticated = True
    # def is_authenticated(self)
    #     return True

    def __str__(self):
        return '%s - %s' % (self.employee_name, self.employee_position)

class EmployeeLogin(models.Model):
    # objects = Employee()
    employee_login = models.OneToOneField(
        Employee,
        to_field='employee_id',
        on_delete=models.CASCADE,
        primary_key = True,
    )
    employee_password = models.CharField(max_length=400)


# class Authority(models.Model):
#     AUTHORITY_CODE  = [
#     ('EMPLOYEE', (
#             ('E1', 'REMOVE_EMPLOYEE'),
#             ('E2', 'ADD_EMPLOYEE'),
#             ('E3', 'UPDATE_EMPLOYEE'),
#             ('E4', 'VIEW_EMPLOYEE'),
#         )
#     ),
#     ('TEAM', (
#             ('T1', 'REMOVE_TEAM'),
#             ('T2', 'ADD_TEAM'),
#             ('T3', 'UPDATE_TEAM'),
#             ('T4', 'VIEW_TEAM'),
#         )
#     ),
#     ('PROJECT', (
#             ('P1', 'REMOVE_PROJECT'),
#             ('P2', 'ADD_PROJECT'),
#             ('P3', 'UPDATE_PROJECT'),
#             ('P4', 'VIEW_PROJECT'),
#     )),
#     ('unknown', 'Unknown')
# ]
#     employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='employee_id')
#     employee_authority = models.CharField(max_length=50, choices=tuple((k,v) for k,v in AUTHORITY_CODE))
#     def __str__(self):
#         return '%s - %s' % (self.employee_id, self.employee_authority[:][:])
