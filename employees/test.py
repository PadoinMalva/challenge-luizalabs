from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Employees
from .serializers import EmployeeSerializer
import datetime


# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_employer(name="", email="", department=""):
        if name != "" and email != "" and department != "":
            # createdAt = datetime.datetime.now()
            Employees.objects.create(
                name=name, email=email, department=department)

    def setUp(self):
        # add test data
        self.create_employer(
            "Daniel malva", "dpmalva@gmail.com", "Dev")
        self.create_employer(
            "Padoin Malva", "padoca@hotmail.com", "Scrum Master")


   
        

class EmployeesTest(BaseViewTest):

    def test_add_new_employee(self):
        data = {
            "name":"Arnaldo Pereira",
            "email":"arnaldao@luizalabs.com.br",
            "department":"Architecture"
        }
        # hit the API endpoint
        response = self.client.post(
            reverse("add-employee"), data, format='json'   
        )
        # fetch the data from db
        expected = Employees.objects.filter(email=data['email'])
        serialized = EmployeeSerializer(expected, many=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data, dict(serialized.data[0]))

       
    def test_get_all_employees(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("employees-all")
        )
        # fetch the data from db
        expected = Employees.objects.all()
        serialized = EmployeeSerializer(expected, many=True)
        self.assertEqual(response.data['results'], serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_destroy_employee(self):
        # hit the API endpoint
        email= 'email=dpmalva@gmail.com'
        
        response = self.client.delete(
            reverse("remove-employee"), QUERY_STRING=email   
        )
        # fetch the data from db

        expected = Employees.objects.filter(email='dpmalva@gmail.com')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)