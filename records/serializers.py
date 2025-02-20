from rest_framework import serializers
from .models import Patient, MedicalRecord, DataExhangeLog

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

class DataExchangeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataExhangeLog
        fields = '__all__'