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
    def create_employer(name="", email="", departament=""):
        if name != "" and email != "" and departament != "":
            createdAt = datetime.datetime.now()
            Employees.objects.create(
                name=name, email=email, departament=departament, createdAt=createdAt)

    def setUp(self):
        # add test data
        self.create_employer(
            "Daniel malva", "dpmalva@gmail.com", "Dev")
        self.create_employer(
            "Padoin Malva", "padoca@hotmail.com", "Scrum Master")


class GetAllEmployeesTest(BaseViewTest):

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
