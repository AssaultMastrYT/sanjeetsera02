from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
from pymongo import MongoClient

#Creating Client
client = MongoClient("mongodb+srv://********:********@cluster0.gbw3x.mongodb.net/?retryWrites=true&w=majority")


def EmployeeDetails(request):
    db = client['EmployeeData']
    collection = db['ActiveEmployees']

    if request.method == "GET":
        employee = request.GET.get('searchEmployee')

        return render(request, 'services/EmployeeDetails.html', {'employee': employee})
    else:
        return render(request, 'services/EmployeeDetails.html')
