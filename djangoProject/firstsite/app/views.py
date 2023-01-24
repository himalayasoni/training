from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Employee, EmployeeSerializer
from .serializers import EmployeeSerializer, UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
#from services import employeeDetailView

# Create your views here.
# @csrf_exempt
# def index (request):
#     print(request.method)
#     if request.method == 'POST':
#         post_data = {'name':request.POST.get('name'),
#                      'email':request.POST.get('email'),
#                      'password':request.POST.get('password'),
#                      'phone':request.POST.get('phone')}
#         print(post_data)
#         response = requests.post(url='http://127.0.0.1:8000/submit', data=post_data)

#         if response.status_code==200:
#             return HttpResponse("Successfully done")
#         else:
#             return HttpResponse("try again")
    
#     # return render(request,template_name="index.html")
#     return render(request, 'index.html')
#     #return HttpResponse("this is home page")

# @csrf_exempt
# def index (request):
#     # print(request.body)
#     if request.method == 'POST':
#         json_data= request.body
#         pythondata=json.loads(json_data)
#         print(pythondata)
#         employeeSerializer = EmployeeSerializer(data = json_data)
#         if employeeSerializer .is_valid():
#             employeeSerializer.save()
#             res={'msg':"Data created"}
#             return json_da(res,safe=False)
#         return 



        # jsonData = JSONParser().parse(request.data)
        # employeeSerializer = EmployeeSerializer(data = jsonData)
        # if employeeSerializer.is_valid():
        #     employeeSerializer.save()
        #     return HttpResponse(employeeSerializer.data, safe=False)
        
        # return HttpResponse(employeeSerializer.errors, safe=False)
    # return HttpResponse('skfd')
def index (request):
    return HttpResponse("home page")

def about (request):
    return HttpResponse("this is about page")

# @csrf_exempt
# def employeeListView (request):
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return JsonResponse(serializer.data, safe = False)
#         # return JsonResponse(serializer.data, safe=False)
#         # return JsonResponse({"message" : "success"})
    
#     elif request.method == 'POST':
#         jsonData = JSONParser().parse(request)
#         serializer = EmployeeSerializer(data = jsonData)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse (serializer.data, safe=False)
#         else:
#             return JsonResponse(serializer.errors, safe = False)



# @csrf_exempt
# def employeeDetailView (request, pk):
#     try:
#         employee = Employee.objects.get(pk=pk)
#         # return JsonResponse("Employee " + str(pk), safe=False)
#     except Employee.DoesNotExist:
#         return HttpResponse(status=404)

    
#     if request.method == 'DELETE':
#         employee.delete()
#         return HttpResponse(status = 200)
    
    
#     elif request.method == 'GET':
#         serializer = EmployeeSerializer(employee)
#         return JsonResponse(serializer.data, safe= False)
    
    
#     elif request.method == 'PUT':
#         jsonData = JSONParser().parse(request)
#         serializer = EmployeeSerializer(employee, data = jsonData)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe = False)
#         else:
#             return JsonResponse (serializer.errors, safe = False)


@api_view(['GET','POST'])
def employeeListView (request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
        # return JsonResponse(serializer.data, safe=False)
        # return JsonResponse({"message" : "success"})
    
    elif request.method == 'POST':
        #jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return Response(serializer.errors)




@api_view(['DELETE','GET', 'PUT'])
def employeeDetailView (request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        
    except Employee.DoesNotExist:
        return Response(status=404)

    
    if request.method == 'DELETE':
        employee.delete()
        return Response(status = 200)
    
    
    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors)

def UserListView(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)