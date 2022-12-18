from django import forms
from models import EmployeeLogin, Employee

class EmployeeForm(forms.ModelForm):
    employee_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = EmployeeLogin
        widgets = {
            'employee_password': forms.PasswordInput()
        }
        fields = '__all__'
