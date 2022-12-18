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
# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

#

class EmployeeList(generics.GenericAPIView,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
