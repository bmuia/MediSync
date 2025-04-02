from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Hospital(models.Model):
    hospital_name = models.CharField(max_length=255)
    hospital_location = models.TextField()
    contact_email = models.EmailField(unique=True)
    hospital_contact = models.CharField(max_length=20)
    hospital_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.hospital_name

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email must be set.')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):

    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('admin', 'Admin'),
        ('patient', 'Patient'),
        ('radiologist', 'Radiologist'),
        ('lab_technician', 'Lab Technician'),
        ('pharmacist', 'Pharmacist'),
        ('data_analyst', 'Data Analyst'),
        ('public_health_official', 'Public Health Official'),
        ('insurance_rep', 'Insurance Representative'),
        ('api_user', 'API User'),
    ]

    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    role = models.CharField(choices=ROLE_CHOICES, max_length=50)
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        return f"{self.email} - {self.role}"
