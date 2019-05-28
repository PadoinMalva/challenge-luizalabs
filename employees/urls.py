from django.urls import include, path
from rest_framework import routers
from employees.views import UserViewSet, GroupViewSet, EmployeeViewSet
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('employees/', EmployeeViewSet.as_view(), name="employees-all")
]
