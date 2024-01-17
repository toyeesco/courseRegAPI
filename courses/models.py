from django.db import models
from authentication.models import Student, Reg_Officer, Hod, Dean

# Create your models here.

class Courses(models.Model):
   COURSE_CHOICE = {
       "SEN401": "SEN401",
       "SEN402": "SEN402",
       "SEN403": "SEN403",
       "SEN404": "SEN404",
       "SEN405": "SEN405",
       "SEN406": "SEN406",
       "SEN407": "SEN407",
       "SEN409": "SEN409"
   }
   name = models.CharField(max_length=100)
   course_code = models.CharField(blank=True, choices=COURSE_CHOICE, max_length=50)
   course_unit = models.IntegerField()

   def __str__(self):
       return self.name

class EnrollmentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    registered_at = models.DateField(auto_now=True)




class Signature(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(EnrollmentCourse, on_delete=models.CASCADE)
    reg_officer = models.ForeignKey(Reg_Officer, related_name="reg_officer", on_delete=models.CASCADE)
    hod = models.ForeignKey(Hod, on_delete=models.CASCADE, related_name="hod")
    dean = models.ForeignKey(Dean, on_delete=models.CASCADE, related_name="dean")

