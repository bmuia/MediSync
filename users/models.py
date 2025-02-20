from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=255)
    hospital_location = models.TextField()
    contact_email = models.EmailField(unique=True)
    hospital_contact = models.CharField(max_length=20)
    hospital_code =  models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.hospital_name
    
    

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin','Admin'),
        ('patient', 'Patient')
    ]
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    role = models.CharField(choices=ROLE_CHOICES,max_length=20,default='patient')
    # Users won't be deleted if a hospital is removed hence opting for SET_NULL rather than using .CASCADE
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL,null=True,blank=True)
    

    def __str__(self):
        return f"{self.email} - {self.role}"