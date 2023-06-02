from django.shortcuts import render
from rest_framework import generics
from .models import Teacher, Student
from .serializers import TeacherSerializers, StudentSerializers
from rest_framework.response import Response


class TeacherlistView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers


class TeacherCreateView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers

    def post(self, request, *args, **kwargs):
        print(request.data.get('name'))
        return Response('no need to fill the name', status=201)


class TeacherDetailView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers


class TeacherDeleteView(generics.DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers


class TeacherUpdateView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
