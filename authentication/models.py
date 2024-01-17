from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_dean = models.BooleanField(default=False)
    is_reg_officer = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)


    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matric_no = models.CharField(unique=True, max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    session = models.CharField(max_length=100)

    def __str__(self):
        return self.matric_no

class Hod(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    signature = models.ImageField(upload_to="images")
    signature_date = models.DateTimeField(auto_now_add=True)

class Reg_Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    signature = models.ImageField(upload_to="images")
    signature_date = models.DateTimeField(auto_now_add=True)

class Dean(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    signature =models.ImageField(upload_to="images")
    signature_date = models.DateTimeField(auto_now_add=True)