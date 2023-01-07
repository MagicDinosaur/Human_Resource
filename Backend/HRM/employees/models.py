from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    objects = None
    DEPARTMENT_CHOICES = (
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Sales', 'Sales'),
        ('Marketing', 'Marketing'),
        ('Finance', 'Finance'),
        ('Operations', 'Operations'),
        ('Others', 'Others'),
    )
    POSITION_CHOICES = (
        ('CEO', 'CEO'),
        ('Manager', 'Manager'),
        ('Senior', 'Senior'),
        ('Junior', 'Junior'),
        ('Trainee', 'Trainee'),
        ('Others', 'Others'),

    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    profile_pic = models.CharField(max_length=800)
    position = models.CharField(max_length=200, choices=POSITION_CHOICES, default='Others')
    department = models.CharField(max_length=200, choices=DEPARTMENT_CHOICES)
    salary = models.CharField(max_length=200)
    date_hired = models.DateField()
    date_left = models.DateField(blank=True, null=True)
    #update later
    class Meta:
        default_permissions = ('view')
        permissions = (('can_view_employee', 'Can view employee'),
                       ('can_add_employee', 'Can add employee')
                       ,('can_change_employee', 'Can change employee'),
                       ('can_delete_employee', 'Can delete employee'),
                       ('can_view_salary', 'Can view salary'))
    def __str__(self):
        return self.user.username + " - " + self.position + " - " +  self.department
    def save(self, *args, **kwargs):
        self.user.email = self.email

        super().save(*args, **kwargs)