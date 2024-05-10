from django.urls import path

from companies.views.employees import Employess, EmployeeDetail
from companies.views.permissions import PermissionDetail

urlpatterns = [
    #  Employee endpoints
    path('employees', Employess.as_view()),
    path('employees/<int:employee_id>', EmployeeDetail.as_view()),

    #  Groups And Permissions Endpoints
    path('permissions', PermissionDetail.as_view()),
]
