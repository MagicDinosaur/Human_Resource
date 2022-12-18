from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Employee

class EmployeeBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        employee_email = request.data.get("username")
        employee_password = request.data.get("password")
        # user = authenticate(username=username, password=password)
        # employee_email = username
        #
        # employee_password = password

        try:
            user = Employee.objects.get(employee_email=employee_email)

            print(user.employee_password)
            # if check_password( employee_password, user.employee_password):
            if user.employee_password == employee_password:
                return user
        except Employee.DoesNotExist:

            return None