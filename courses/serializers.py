from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"

class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentCourse
        fields = "__all__"

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = "__all__"