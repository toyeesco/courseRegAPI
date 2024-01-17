from django.urls import path
from .views import (
    SignUpView,
    StudentListView,
    StudentDetailView,
    HodListView,
    HodDetailView,
    RegOfficerListView,
    RegOfficerDetailView,
    DeanListView,
    DeanDetailView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('student-create/', StudentListView.as_view(), name='list-create'),
    path('student-detail/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),

    path('hod-list/', HodListView.as_view(), name='list-create'),
    path('hod-detail/<int:pk>/', HodDetailView.as_view(), name='hod-detail'),

    path('reg-officer/', RegOfficerListView.as_view(), name='reg-officer-list'),
    path('reg-officer-detail/<int:pk>/', RegOfficerDetailView.as_view(), name='reg-officer-detail'),

    path('dean/', DeanListView.as_view(), name='dean-list'),
    path('dean-detail/<int:pk>/', DeanDetailView.as_view(), name='dean-detail'),

    path('jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),


]