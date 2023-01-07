from django.urls import path
from .views import *

urlpatterns = [
    path('list/', employee_list, name='employee-list'),
    path('test/', test_view, name='test-view'),
    # path('employees/create/', EmployeeCreate.as_view(), name='employee-create'),
    ]