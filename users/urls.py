from django.urls import path
from .views import DoctorOnlyView, AdminOnlyView, NurseOnlyView, PatientOnlyView,RegisterView,CustomTokenObtainPairView, HospitalAPIView, HospitalCreateAPIView, HospitalDetailAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)



urlpatterns = [
    path('doctor/', DoctorOnlyView.as_view(), name='doctor-only'),
    path('admin/', AdminOnlyView.as_view(), name='admin-only'),
    path('nurse/', NurseOnlyView.as_view(), name='nurse-only'),
    path('patient/', PatientOnlyView.as_view(), name='patient-only'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('login/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('hospitals/', HospitalAPIView.as_view(), name='hospital-list'),
    path('hospitals/create/', HospitalCreateAPIView.as_view(), name='hospital-create'),
    path('hospitals/<int:pk>/', HospitalDetailAPIView.as_view(), name='hospital-detail'),
]
