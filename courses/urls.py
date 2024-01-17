from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    EnrollmentCreateCourseView,
    EnrollmentCourseDetailView,
    SignatureListView,
    SignatureDetailView
)

urlpatterns = [
    path('course-create/', CourseListView.as_view(), name='list-create'),
    path('course-detail/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('enroll-create/', EnrollmentCreateCourseView.as_view(), name='enroll-list-create'),
    path('enroll-detail/<int:pk>/', EnrollmentCourseDetailView.as_view(), name='enroll-detail'),
    path('signature-create/', SignatureListView.as_view(), name='signature-create'),
    path('signature-detail/<int:pk>/', SignatureDetailView.as_view(), name='signature-detail')

]