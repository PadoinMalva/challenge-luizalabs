from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from employees.serializers import UserSerializer, GroupSerializer, EmployeeSerializer
from employees.models import Employees
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404



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


class EmployeeCreateViewSet(generics.CreateAPIView):
    print('Entrei No create')
    serializer_class = EmployeeSerializer


class EmployeeListViewSet(generics.ListAPIView):
    print('Entrei no LIST')
    queryset = Employees.objects.all().order_by('-createdAt')
    serializer_class = EmployeeSerializer


class EmployeeRemoveViewSet(generics.DestroyAPIView):
    print('Entrei no Remove')
    lookup_field = 'email'
    serializer_class = EmployeeSerializer

    def get_object(self):
        email= self.request.META['QUERY_STRING'].split('=')[1]
        return get_object_or_404(Employees, email=email)
     
        
        

