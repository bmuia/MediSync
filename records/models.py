from django.db import models
from users.models import Hospital, CustomUser
from encrypted_model_fields.fields import EncryptedTextField
# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'patient'}, null=True,blank=True)
    medical_record_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.user} - {self.medical_record_number}"


class DiagnosisRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True,blank=True)
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'},null=True,blank=True)
    diagnosis = EncryptedTextField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnosis for {self.patient} by {self.doctor}"

class TreatmentPlan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True,blank=True)
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'},null=True,blank=True)
    treatment_plan = EncryptedTextField(null=True, blank=True)
    treatment_details = EncryptedTextField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Treatment Plan for {self.patient}"

class MedicationRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True,blank=True) 
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'},null=True,blank=True)      
    drug_name = EncryptedTextField()  
    dosage = EncryptedTextField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medication for {self.patient}: {self.drug_name}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True,blank=True)
    diagnosis = models.ForeignKey(DiagnosisRecord, on_delete=models.CASCADE, null=True, blank=True)
    treatment = models.ForeignKey(TreatmentPlan, on_delete=models.CASCADE, null=True, blank=True)
    medication = models.ForeignKey(MedicationRecord, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Record for {self.patient}"
    
class DataExchangeLog(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null= True,blank=True)
    source_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="source_hospital",null=True,blank=True)
    # Assuming Hospital is a model that represents hospitals in your system
    destination_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="destination_hospital",null=True,blank=True)  
    requested_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="requested_by",null=True,blank=True)    
    approved_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name="approved_by")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data request for {self.patient} from {self.source_hospital} to {self.destination_hospital}"


class APIAccessLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)  
    endpoint = models.CharField(max_length=255)  
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True) 
    ip_address = models.GenericIPAddressField(null=True, blank=True)  
    status_code = models.IntegerField()

    def __str__(self):
        return f"{self.user} accessed {self.endpoint} ({self.method}) at {self.timestamp}"