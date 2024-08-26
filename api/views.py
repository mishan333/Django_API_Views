from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response 
'''function base''' 
from rest_framework.decorators import api_view
'''class base'''
from rest_framework.views import APIView

from rest_framework import status

from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, 
    UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
)

from rest_framework.generics import GenericAPIView

from .models import *
from .serializers import *
from rest_framework import viewsets

class Student_Viewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
'''
#? Viewsets
class Student_Viewset(viewsets.ViewSet):
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)
'''

'''
class student_list(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request): 
        return self.create(request)

class student_details(
    GenericAPIView, RetrieveModelMixin,DestroyModelMixin, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''

'''
#? Class Based View
class student_list(APIView):
    def get(self,request):
        student=Student.objects.all()
        serializer = StudentSerializer(student , many=True)
        return Response(serializer.data, status.HTTP_202_ACCEPTED)
    
    def post(self , request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class student_details(APIView ):
    def get(self , request , pk):
        student = get_object_or_404(Student,pk=pk) 
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self, request , pk ):
        student = get_object_or_404(Student,pk=pk) 
        serializer= StudentSerializer(student,data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data , status= status.HTTP_201_CREATED)

    def delete(self,request,pk):
        student = get_object_or_404(Student,pk=pk) 
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''
#? Function Based View
@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'POST':
        serializer= StudentSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data , status= status.HTTP_201_CREATED)
    else:
        student = Student.objects.all()
        serializer = StudentSerializer(student, many = True)
        return Response(serializer.data)
    
@api_view (['GET','PUT','DELETE'])
def student_view(request , pk):
    # student = Student.objects.get(pk=pk) 
    student = get_object_or_404(Student,pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''