from django.urls import path
from .views import PatientAPiView, PatientCreateAPIView, PatientDetailAPIView, MedicalRecordListAPIView, MedicalRecordCreateAPIView, MedicalRecordDetailAPIView, DataExchangeLogListAPIView, DataExchangeLogCreateAPIView, DataExchangeLogDetailAPIView


urlpatterns = [
    path('patients/', PatientAPiView.as_view(), name='patient-list'),
    path('patient/create/', PatientCreateAPIView.as_view(), name='patient-create'),
    path('patient/<int:pk>', PatientDetailAPIView.as_view(), name='patient-detail'),

    path('medical-records/', MedicalRecordListAPIView.as_view(), name='medical-record-list'),
    path('medical-records/create/', MedicalRecordCreateAPIView.as_view(), name='medical-record-create'),
    path('medical-records/<int:pk>/', MedicalRecordDetailAPIView.as_view(), name='medical-record-detail'),


    path('data-exchange/', DataExchangeLogListAPIView.as_view(), name='data-exchange-list'),
    path('data-exchange/create/', DataExchangeLogCreateAPIView.as_view(), name='data-exchange-create'),
    path('data-exchange/<int:pk>/', DataExchangeLogDetailAPIView.as_view(), name='data-exchange-detail'),
]
