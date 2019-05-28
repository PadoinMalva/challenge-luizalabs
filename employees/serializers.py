from django.contrib.auth.models import User, Group
from rest_framework import serializers
from employees.models import Employees

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('name','email','departament')