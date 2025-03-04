from django.contrib import admin
from .models import Patient, MedicalRecord, DataExhangeLog

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'date_of_birth', 'hospital', 'medical_record_number')
    search_fields = ('first_name', 'last_name', 'medical_record_number')
    list_filter = ('hospital', 'gender')

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'hospital', 'created_at', 'updated_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__email')
    list_filter = ('hospital', 'doctor')

class DataExhangeLogAdmin(admin.ModelAdmin):
    list_display = ('patient', 'source_hospital', 'destination_hospital', 'requested_by', 'approved_by', 'status', 'timestamp')
    search_fields = ('patient__first_name', 'patient__last_name', 'source_hospital__hospital_name', 'destination_hospital__hospital_name')
    list_filter = ('status', 'source_hospital', 'destination_hospital')

admin.site.register(Patient, PatientAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(DataExhangeLog, DataExhangeLogAdmin)
