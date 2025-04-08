from django.urls import path
from .views import (FHIRPatientCreateAPIView,
                    FHIRPatientRetrieveAPIView,
                    FHIRPatientUpdateAPIView,
                    FHIRPatientDeleteAPIView,
                    DiagnosisCreateAPIView,
                    TreatmentPlanCreateAPIView,
                    MedicationCreateAPIView,
                    MedicalRecordListAPIView, 
                    DataExchangeLogListAPIView, 
                    DataExchangeLogCreateAPIView, 
                    DataExchangeLogDetailAPIView,
                    ReceiveFHIRPatientView,ApproveAndTransferPatientView,
                    DiagnosisListAPIView,
                    TreatmentPlanListView,
                    MedicationListAPIView
                    )


urlpatterns = [
    path('fhir/patient/create/', FHIRPatientCreateAPIView.as_view(), name='fhir-patient-create'),
    path('fhir/patient/<int:pk>/', FHIRPatientRetrieveAPIView.as_view(), name='fhir-patient-retrieve'),
    path('fhir/patient/update/<int:pk>/', FHIRPatientUpdateAPIView.as_view(), name='fhir-patient-update'),
    path('fhir/patient/delete/<int:pk>/', FHIRPatientDeleteAPIView.as_view(), name='fhir-patient-delete'),
    path('diagnosis/', DiagnosisListAPIView.as_view(), name='diagnosis-list'),


    path('diagnosis/create/', DiagnosisCreateAPIView.as_view(), name='diagnosis-create'),
    path('treatment-plan/', TreatmentPlanListView.as_view(), name='treatment-plan'),
    path('treatment/create/', TreatmentPlanCreateAPIView.as_view(), name='treatment-create'),
    path('medication/create/', MedicationCreateAPIView.as_view(), name='medication-create'),
    path('medication/', MedicationListAPIView.as_view(), name='medication-list' ),
    path('medical-records/', MedicalRecordListAPIView.as_view(), name='medical-records'),

    path('fhir/patient/receive/', ReceiveFHIRPatientView.as_view(), name='fhir-patient-receive'),
    path('data-exchange/transfer/<int:log_id>/', ApproveAndTransferPatientView.as_view(), name='data-exchange-transfer'),
    path('data-exchange/', DataExchangeLogListAPIView.as_view(), name='data-exchange-list'),
    path('data-exchange/create/', DataExchangeLogCreateAPIView.as_view(), name='data-exchange-create'),
    path('data-exchange/<int:pk>/', DataExchangeLogDetailAPIView.as_view(), name='data-exchange-detail'),
]
