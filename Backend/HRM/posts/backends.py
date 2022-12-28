from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Employee, EmployeeLogin

class EmployeeBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # employee_email = request.data.get("username")
        # employee_password = request.data.get("password")
        employee_email = username
        employee_password = password
        print(employee_email, employee_password)
        try:
            user = Employee.objects.get(employee_email=employee_email)
            user_password = EmployeeLogin.objects.get(employee_login_id = int(user.employee_id)).employee_password
            # if check_password( employee_password, user_password):
            if user_password == str(employee_password):
                user.is_anonymous= False
                user.is_authenticated = True
                # user.save()
                return user
            else:
                return None
        except Employee.DoesNotExist:
            return None
