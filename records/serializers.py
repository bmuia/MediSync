from rest_framework import serializers
from .models import Patient, MedicalRecord, DiagnosisRecord, TreatmentPlan, MedicationRecord,DataExchangeLog
from users.serializers import HospitalSerializer,UserSerializer
from users.models import Hospital
class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

class DiagnosisSerializer(serializers.ModelSerializer):
    doctor = UserSerializer()
    class Meta:
        model = DiagnosisRecord
        fields = '__all__'

class TreatmentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentPlan
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationRecord
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    diagnosis = DiagnosisSerializer()
    treatment = TreatmentPlanSerializer()
    medication = MedicationSerializer()
    
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        
class DataExchangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataExchangeLog
        fields = '__all__'