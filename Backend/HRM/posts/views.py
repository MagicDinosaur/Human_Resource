from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Employee, Authority
from .serializers import EmployeeSerializer, AuthoritySerializer, EmployeeLoginSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.views import View
# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication

#


class EmployeeList(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self):
        pass




# class EmployeeList(generics.GenericAPIView,
#                    mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,):
#     # authentication_classes = [TokenAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Employee.objects.all()
#     # queryset = Employee.objects.filter(employee_id=id).first()
#     serializer_class = EmployeeSerializer
#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)

# class EmployeeLogin(View):
#     def post(self, request):
#         employee_email = request.POST['employee_email']
#         employee_password = request.POST['employee_password']
#         user = authenticate(username=employee_email, password=employee_password)
#         if user is not None:
#             user.is_anonymous = False
#             user.is_authenticated = True
#             return HttpResponse('success')
#         else:
#             return HttpResponse('failed')
#
