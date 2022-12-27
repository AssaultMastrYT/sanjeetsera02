from django.urls import path
from . import views

urlpatterns = [
    path('employeedetails/', views.EmployeeDetails, name='EmployeeDetails'),
]