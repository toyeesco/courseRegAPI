from django.shortcuts import render
from .serializers import CourseSerializer, SignatureSerializer, EnrollSerializer
from rest_framework import generics
from .models import Courses, Signature, EnrollmentCourse
from .serializers import CourseSerializer, EnrollSerializer
# Create your views here.

class CourseListView(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

class EnrollmentCreateCourseView(generics.ListCreateAPIView):
    queryset = EnrollmentCourse.objects.all()
    serializer_class = EnrollSerializer

class EnrollmentCourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnrollmentCourse.objects.all()
    serializer_class = EnrollSerializer

class SignatureListView(generics.ListCreateAPIView):
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer


class SignatureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Signature.objects.all()
    serializer_class = SignatureSerializer
