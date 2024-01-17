from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from .models import User, Student, Hod, Reg_Officer, Dean
from .serializers import SignUpSerializer, StudentSerializer, HodSerializer, RegOfficerSerializer, DeanSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "User Created Successfully",
                "data": serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class HodListView(generics.ListCreateAPIView):
    queryset = Hod.objects.all()
    serializer_class = HodSerializer

class HodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hod.objects.all()
    serializer_class = HodSerializer

class RegOfficerListView(generics.ListCreateAPIView):
    queryset = Reg_Officer.objects.all()
    serializer_class = HodSerializer

class RegOfficerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reg_Officer.objects.all()
    serializer_class = HodSerializer

class DeanListView(generics.ListCreateAPIView):
    queryset = Dean.objects.all()
    serializer_class = HodSerializer

class DeanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dean.objects.all()
    serializer_class = HodSerializer