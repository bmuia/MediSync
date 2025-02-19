from django.db import models
from users.models import Hospital, CustomUser
# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    date_of_birth = models.CharField(max_length=10)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    medical_record_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Patient is {self.first_name} {self.last_name}"


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'doctor'})
    diagonis = models.TextField()
    treatment_plan = models.TextField()
    treatment_drugs = models.TextField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patient record for {self.patient} by {self.doctor} whose diagnosis is{self.diagonis} and so on"
    
class DataExhangeLog(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    source_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="source_hospital")
    destination_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="destination_hospital")
    requested_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="requested_by")
    approved_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name="approved_by")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data request for {self.patient} from {self.source_hospital} to {self.destination_hospital}"