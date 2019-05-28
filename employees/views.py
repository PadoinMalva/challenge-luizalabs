from django.contrib.auth.models import User, Group
from rest_framework import viewsets,generics
from employees.serializers import UserSerializer, GroupSerializer, EmployeeSerializer
from employees.models import Employees


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class EmployeeViewSet(generics.ListAPIView):
    queryset = Employees.objects.all().order_by('-createdAt')
    serializer_class = EmployeeSerializer