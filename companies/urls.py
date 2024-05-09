from django.urls import path

from companies.views.employees import Employess, EmployeeDetail 

urlpatterns = [
    #  Employee endpoints
    path('employees', Employess.as_view()),
    path('employees/<int:employee_id>', EmployeeDetail.as_view())
]
