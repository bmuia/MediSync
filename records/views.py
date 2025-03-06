from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsDoctor, IsNurse, IsAdmin
from .serializers import PatientSerializer, MedicalRecordSerializer, DataExchangeLogSerializer,DiagnosisSerializer, TreatmentPlanSerializer, MedicationSerializer
from .models import Patient, MedicalRecord, DataExhangeLog, DiagnosisRecord, TreatmentPlan, MedicationRecord

# PATIENT VIEWS
class PatientAPiView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientCreateAPIView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated | IsAdmin | IsDoctor] 

class PatientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated | IsAdmin | IsDoctor] 

# MEDICAL RECORD VIEWS
class DiagnosisCreateAPIView(generics.CreateAPIView):
    queryset = DiagnosisRecord.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

class TreatmentPlanCreateAPIView(generics.CreateAPIView):
    queryset = TreatmentPlan.objects.all()
    serializer_class = TreatmentPlanSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

class MedicationCreateAPIView(generics.CreateAPIView):
    queryset = MedicationRecord.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

class MedicalRecordListAPIView(generics.ListAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsDoctor]

# DATA EXCHANGE LOG VIEWS
class DataExchangeLogListAPIView(generics.ListAPIView):
    queryset = DataExhangeLog.objects.all()
    serializer_class = DataExchangeLogSerializer
    permission_classes = [IsAuthenticated, IsAdmin]  

class DataExchangeLogCreateAPIView(generics.CreateAPIView):
    queryset = DataExhangeLog.objects.all()
    serializer_class = DataExchangeLogSerializer
    permission_classes = [IsAuthenticated | IsDoctor | IsNurse] 

class DataExchangeLogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataExhangeLog.objects.all()
    serializer_class = DataExchangeLogSerializer
    permission_classes = [IsAuthenticated, IsAdmin]  
