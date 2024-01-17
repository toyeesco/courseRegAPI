from rest_framework import serializers
from .models import *


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="User with username exists")

        email_exists = User.objects.filter(username=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class HodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hod
        fields = "__all__"

class RegOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg_Officer
        fields = "__all__"

class DeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dean
        fields = "__all__"