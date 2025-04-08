from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.permissions import IsDoctor, IsNurse, IsAdmin,IsPatient
from .serializers import PatientSerializer, MedicalRecordSerializer, DataExchangeLogSerializer, DiagnosisSerializer, TreatmentPlanSerializer, MedicationSerializer
from .models import Patient, MedicalRecord, DiagnosisRecord, TreatmentPlan, MedicationRecord, DataExchangeLog
from fhir.resources.patient import Patient as FHIRPatient
from .fhir_utils import create_fhir_patient,send_patient_data_to_hospital,transfer_patient_data

class FHIRPatientCreateAPIView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated | IsAdmin | IsDoctor]

    def perform_create(self, serializer):
        patient = serializer.save()
        fhir_patient = create_fhir_patient(patient)
        return Response(fhir_patient, status=201)

# ✅ API to receive FHIR patient data
class ReceiveFHIRPatientView(APIView):
    def post(self, request):
        data = request.data.get("patient", {})
        medical_record_number = data.get("id")

        patient, created = Patient.objects.get_or_create(
            medical_record_number=medical_record_number,
            defaults={"user": None},
        )

        return Response({"message": "Patient data received successfully"}, status=status.HTTP_201_CREATED)

# ✅ API to approve & transfer patient data
class ApproveAndTransferPatientView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, log_id):
        destination_hospital_api_url = "http://127.0.0.1:8000/api/fhir/patient/receive/"


        success = transfer_patient_data(log_id, destination_hospital_api_url)
        
        if success:
            return Response({"message": "Data transferred successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "Data transfer failed"}, status=status.HTTP_400_BAD_REQUEST)

class FHIRPatientRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def retrieve(self, request, *args, **kwargs):
        patient = self.get_object()
        fhir_patient = create_fhir_patient(patient)
        return Response(fhir_patient)

class FHIRPatientUpdateAPIView(generics.UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def perform_update(self, serializer):
        patient = serializer.save()
        fhir_patient = create_fhir_patient(patient)
        return Response(fhir_patient.dict(), status=200)

class FHIRPatientDeleteAPIView(generics.DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        return Response(status=204)
    

class DiagnosisListAPIView(generics.ListAPIView):
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated |IsAdmin | IsPatient | IsDoctor]

    def get_queryset(self):
        # Filter by the currently authenticated user (patient)
        user = self.request.user  # Get the currently logged-in user
        # Return diagnosis records for this patient
        return DiagnosisRecord.objects.filter(patient__user=user)
    
class TreatmentPlanListView(generics.ListAPIView):
    queryset = TreatmentPlan.objects.all()
    serializer_class = TreatmentPlanSerializer
    permission_classes = [IsAuthenticated | IsPatient | IsAdmin]

class DiagnosisCreateAPIView(generics.CreateAPIView):
    queryset = DiagnosisRecord.objects.all()
    serializer_class = DiagnosisSerializer
    permission_classes = [IsAuthenticated, IsDoctor]



class TreatmentPlanCreateAPIView(generics.CreateAPIView):
    queryset = TreatmentPlan.objects.all()
    serializer_class = TreatmentPlanSerializer
    permission_classes = [IsAuthenticated, IsDoctor]

class MedicationListAPIView(generics.ListAPIView):
    queryset = MedicationRecord.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated | IsDoctor | IsPatient]

class MedicationCreateAPIView(generics.CreateAPIView):
    queryset = MedicationRecord.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated, IsDoctor]



class MedicalRecordListAPIView(generics.ListAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated | IsAdmin | IsDoctor]

class DataExchangeLogListAPIView(generics.ListAPIView):
    queryset = DataExchangeLog.objects.all()
    serializer_class = DataExchangeLogSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

class DataExchangeLogCreateAPIView(generics.CreateAPIView):
    queryset = DataExchangeLog.objects.all()
    serializer_class = DataExchangeLogSerializer
    permission_classes = [IsAuthenticated | IsDoctor | IsNurse]

class DataExchangeLogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataExchangeLog.objects.all()
    serializer_class = DataExchangeLogSerializer
    permission_classes = [IsAuthenticated, IsAdmin]