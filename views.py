from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


#def home(request):
    #return render(request,'home.html')

@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs , many=True)
    return Response({'status':200, 'message' : 'serializer.data'})


@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs , many=True)
    return Response({'status':200, 'message' : 'serializer.data'})

@api_view(['POST'])
def post_student(request):
    data = request.data
    serializer = StudentSerializer(data)

    if request.data['age']<18:
        return Response({'status':403,'message' : 'age mst be >18'})

    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':403, 'errors':serializer.errors,'message' : 'Something went worng'})
    
    serializer.save()

    return Response({'status':200,'payload': serializer.data ,'message' : 'your data is saved.'})

@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj=Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj,data=request.data,partial=True)  #partial=True meance this method is patch 
        #serializer = StudentSerializer(student_obj,data=request.data) #this method is put 
        if request.data['age']<18:
            return Response({'status':403,'message' : 'age mst be >18'})

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'errors':serializer.errors,'message' : 'Something went worng'})
        
        serializer.save()

        return Response({'status':200,'payload': serializer.data ,'message' : 'your data is saved.'})
    except Exception as e:
        return Response({'status':403,'message' : 'invalid id'})
    
@api_view(['DELETE'])
def delete_student(request):
    try:
        id = request.GET.get('id')
        sudent_obj=Student.objects.get(id=id)
        sudent_obj.delete()
        return Response({'status':200,'message' : 'delete'})
        
    except Exception as e:
        return Response({'status':403,'message' : 'invalid id'})