from django.contrib import admin
from .models import (
    Patient, DiagnosisRecord, TreatmentPlan, MedicationRecord, MedicalRecord, DataExhangeLog, APIAccessLog
)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'date_of_birth', 'hospital', 'medical_record_number')
    search_fields = ('first_name', 'last_name', 'medical_record_number')
    list_filter = ('hospital', 'gender')

class DiagnosisRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__email')
    list_filter = ('doctor',)

class TreatmentPlanAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__email')
    list_filter = ('doctor',)

class MedicationRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'drug_name', 'dosage', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__email', 'drug_name')
    list_filter = ('doctor',)

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name')

class DataExchangeLogAdmin(admin.ModelAdmin):  
    list_display = ('patient', 'source_hospital', 'destination_hospital', 'requested_by', 'approved_by', 'status', 'timestamp')
    search_fields = ('patient__first_name', 'patient__last_name', 'source_hospital__hospital_name', 'destination_hospital__hospital_name')
    list_filter = ('status', 'source_hospital', 'destination_hospital')

class APIAccessLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'endpoint', 'method', 'status_code', 'timestamp', 'ip_address')
    list_filter = ('method', 'status_code', 'timestamp')
    search_fields = ('user__email', 'endpoint', 'ip_address')
# Register models
admin.site.register(Patient, PatientAdmin)
admin.site.register(DiagnosisRecord, DiagnosisRecordAdmin)
admin.site.register(TreatmentPlan, TreatmentPlanAdmin)
admin.site.register(MedicationRecord, MedicationRecordAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(DataExhangeLog, DataExchangeLogAdmin)  
admin.site.register(APIAccessLog, APIAccessLogAdmin)
