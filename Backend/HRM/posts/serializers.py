from rest_framework import serializers
from .models import Employee, Authority, AdminView, EmployeeLogin
from django.contrib.auth.hashers import make_password
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    validate_password = make_password
class AuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Authority
        fields = '__all__'

class EmployeeLoginSerializer(serializers.ModelSerializer):
    employee_password = serializers.CharField(style={'input_type': 'password'})
    class Meta:
        model = EmployeeLogin
        fields = '__all__'