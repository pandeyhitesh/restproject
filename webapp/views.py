from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializer import employeeSerializer

class employeeList(APIView):
    def get(self, request):
        emp = employees.objects.all()
        serializer = employeeSerializer(emp, many = True)
        return Response(serializer.data)


    def post(self):
        pass