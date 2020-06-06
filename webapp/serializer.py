from rest_framework import serializers
from . models import employees

class employeeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = employees
        
        fields='__all__'
