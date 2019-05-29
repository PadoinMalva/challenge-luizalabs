from django.urls import include, path
from rest_framework import routers
from employees.views import UserViewSet, GroupViewSet, EmployeeCreateViewSet, EmployeeListViewSet, EmployeeRemoveViewSet
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('employ/addemployee', EmployeeCreateViewSet.as_view(), name="add-employ" ),
    path('employees/', EmployeeListViewSet.as_view(), name="employees-all"),
    path('employ/removeemployee', EmployeeRemoveViewSet.as_view(), name="remove-employ" )
]
