from django.urls import path
from .views import DoctorOnlyView, AdminOnlyView, NurseOnlyView, PatientOnlyView,RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('doctor/', DoctorOnlyView.as_view(), name='doctor-only'),
    path('admin/', AdminOnlyView.as_view(), name='admin-only'),
    path('nurse/', NurseOnlyView.as_view(), name='nurse-only'),
    path('patient/', PatientOnlyView.as_view(), name='patient-only'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
    path('login/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
