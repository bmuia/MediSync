from django.urls import path
from .views import (PatientAPiView, 
                    PatientCreateAPIView, 
                    PatientDetailAPIView,
                    DiagnosisCreateAPIView,
                    TreatmentPlanCreateAPIView,
                    MedicationCreateAPIView,
                    MedicalRecordListAPIView, 
                    DataExchangeLogListAPIView, 
                    DataExchangeLogCreateAPIView, 
                    DataExchangeLogDetailAPIView)


urlpatterns = [
    path('patients/', PatientAPiView.as_view(), name='patient-list'),
    path('patient/create/', PatientCreateAPIView.as_view(), name='patient-create'),
    path('patient/<int:pk>', PatientDetailAPIView.as_view(), name='patient-detail'),


    path('diagnosis/create/', DiagnosisCreateAPIView.as_view(), name='diagnosis-create'),
    path('treatment/create/', TreatmentPlanCreateAPIView.as_view(), name='treatment-create'),
    path('medication/create/', MedicationCreateAPIView.as_view(), name='medication-create'),
    path('medical-records/', MedicalRecordListAPIView.as_view(), name='medical-records'),


    path('data-exchange/', DataExchangeLogListAPIView.as_view(), name='data-exchange-list'),
    path('data-exchange/create/', DataExchangeLogCreateAPIView.as_view(), name='data-exchange-create'),
    path('data-exchange/<int:pk>/', DataExchangeLogDetailAPIView.as_view(), name='data-exchange-detail'),
]
