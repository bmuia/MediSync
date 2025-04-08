from django.contrib import admin
from .models import (
    Patient, DiagnosisRecord, TreatmentPlan, MedicationRecord, MedicalRecord, APIAccessLog, DataExchangeLog
)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'medical_record_number')
    search_fields = ('user__first_name', 'user__last_name', 'medical_record_number')

    
class DiagnosisRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'created_at')
    search_fields = ('patient__user__first_name', 'patient__user__last_name', 'doctor__email')  # CustomUser fields
    list_filter = ('doctor',)

# Admin for Treatment Plan
class TreatmentPlanAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'created_at')
    search_fields = ('patient__user__first_name', 'patient__user__last_name', 'doctor__email')  # CustomUser fields
    list_filter = ('doctor',)

# Admin for Medication Record
class MedicationRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'drug_name', 'dosage', 'created_at')
    search_fields = ('patient__user__first_name', 'patient__user__last_name', 'doctor__email', 'drug_name')
    list_filter = ('doctor',)

# Admin for Medical Record
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'created_at')
    search_fields = ('patient__user__first_name', 'patient__user__last_name')

# Admin for DataExchangeLog
class DataExchangeLogAdmin(admin.ModelAdmin):
    list_display = ('patient', 'source_hospital', 'destination_hospital', 'requested_by', 'approved_by', 'status', 'timestamp')
    search_fields = (
        'patient__user__first_name', 'patient__user__last_name',
        'source_hospital__hospital_name', 'destination_hospital__hospital_name'
    )
    list_filter = ('status', 'source_hospital', 'destination_hospital')

# Admin for APIAccessLog
class APIAccessLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'endpoint', 'method', 'status_code', 'timestamp', 'ip_address')
    list_filter = ('method', 'status_code', 'timestamp')
    search_fields = ('user__email', 'endpoint', 'ip_address')



# Register models in the admin panel
admin.site.register(Patient, PatientAdmin)
admin.site.register(DiagnosisRecord, DiagnosisRecordAdmin)
admin.site.register(TreatmentPlan, TreatmentPlanAdmin)
admin.site.register(MedicationRecord, MedicationRecordAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(DataExchangeLog, DataExchangeLogAdmin)
admin.site.register(APIAccessLog, APIAccessLogAdmin)
