from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . serializers import StudentSerializer
from .models import Student
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("hello")

def homepage(request):
    return render(request, 'FirstApp/homepage.html')

@csrf_exempt
def AllStudentDetails(request):
    try:
        all_student = Student.objects.all()
    except:
        return HttpResponse("Data not presnet", status = 404)

    if request.method == 'GET':
        students = StudentSerializer(all_student, many=True)
        return JsonResponse(students.data, safe=False)
    
    elif request.method == 'POST':
        input_data = JSONParser().parse(request)
        serializer = StudentSerializer(data = input_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return HttpResponse("Invalid data", status=400)
        
def SingleStudentDetails(request, pk):
    try:
        student = Student.objects.get(pk = pk)
    except:
        return HttpResponse('Data not found', status = 400)
    
    if request.method == 'GET':
        students_data = StudentSerializer(student)
        return JsonResponse(students_data.data, status = 200)
    
    elif request.method == 'PUT':
        update_data = JSONParser().parse(request)
        serializer = StudentSerializer(student, data = update_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        else:
            return HttpResponse("Invalid data", status=400)
        
    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse("Successfully delete", status = 204)
