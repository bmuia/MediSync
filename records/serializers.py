from rest_framework import serializers
from .models import Patient, MedicalRecord, DiagnosisRecord, TreatmentPlan, MedicationRecord,DataExhangeLog
from users.serializers import HospitalSerializer
from users.models import Hospital
class PatientSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer(read_only=True)  # For fetching hospital details
    hospital_id = serializers.PrimaryKeyRelatedField(
        queryset=Hospital.objects.all(), source="hospital", write_only=True
    )  # For creating a patient with hospital ID

    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'gender', 'date_of_birth', 
                  'medical_record_number', 'hospital', 'hospital_id']

class DiagnosisSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        
class DataExchangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataExhangeLog
        fields = '__all__'