from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from guardian.shortcuts import get_objects_for_user


# @permission_required('employees.can_view_employee')
@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
@permission_required('employees.can_view_employee')
def employee_list(request):
    #raise exeption if user is not authenticated or does not have permission
    # print("hello")
    response = {'success': False,
                'error': None,
                'message': ''}
    if request.method == 'GET':
        # user = Employee.objects.get(user=user_id)
        # serializer = EmployeeSerializer(user)
        if request.user.has_perms(['employees.can_view_employee']):
            if not request.user.has_perm('employees.can_view_salary'):
                employee = Employee.objects.all().only('address', 'date_hired')
                response['message'] = 'Employee data retrieved successfully- None salary'
                serializer = EmployeeSerializer(employee, many=True, fields=('address', 'date_hired'))
            else:

                employee = Employee.objects.all()
                response['message'] = 'Employee data retrieved successfully'
                serializer = EmployeeSerializer(employee, many=True)
            response['success'] = True
            response['data'] = serializer.data
            return Response(response)
    # employee_list = Employee.objects.all()
    # serializer = EmployeeSerializer(employee_list, many=True)
    # return Response(serializer.data)

    return Response("User is not authenticated or does not have permission")

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def test_view(request):
    return HttpResponse("test")

