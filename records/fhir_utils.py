import requests  # Ensure you have requests installed
from fhir.resources.patient import Patient
from fhir.resources.humanname import HumanName
from fhir.resources.contactpoint import ContactPoint
from fhir.resources.address import Address
from .models import DataExchangeLog
from datetime import datetime

# Helper function to serialize datetime objects
def serialize_fhir_data(fhir_data):
    if isinstance(fhir_data, dict):
        for key, value in fhir_data.items():
            fhir_data[key] = serialize_fhir_data(value)
    elif isinstance(fhir_data, list):
        for i in range(len(fhir_data)):
            fhir_data[i] = serialize_fhir_data(fhir_data[i])
    elif isinstance(fhir_data, datetime):
        return fhir_data.isoformat()  # Convert datetime to ISO format string
    return fhir_data



# ✅ Function to create FHIR patient data
def create_fhir_patient(patient):
    fhir_patient = Patient.construct()
    fhir_patient.id = patient.medical_record_number
    fhir_patient.name = [
        HumanName(family=patient.user.last_name, given=[patient.user.first_name])
    ]
    fhir_patient.telecom = [
        ContactPoint(system="phone", value=patient.user.email)
    ]
    fhir_patient.address = [
        Address(
            line=[patient.user.hospital.hospital_location],
            city=patient.user.hospital.hospital_name
        )
    ]
    return fhir_patient.dict()  # Convert to JSON format

# ✅ Function to send FHIR data to another hospital
def send_patient_data_to_hospital(destination_hospital_api_url, fhir_data):
    fhir_data = serialize_fhir_data(fhir_data)  # Serialize datetime fields
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer <destination_hospital_api_token>',  # Replace with actual token
    }

    try:
        response = requests.post(destination_hospital_api_url, json=fhir_data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 4xx or 5xx)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error sending patient data: {e}")
        return False

# ✅ Function to update the data exchange log
def update_data_exchange_log(log_id, status='approved'):
    try:
        log = DataExchangeLog.objects.get(id=log_id)
        log.status = status
        log.save()
        return True
    except DataExchangeLog.DoesNotExist:
        return False

# ✅ Function to handle the full transfer
def transfer_patient_data(log_id, destination_hospital_api_url):
    try:
        log = DataExchangeLog.objects.get(id=log_id)
    except DataExchangeLog.DoesNotExist:
        return False  # Return False if the log does not exist

    if log.status != 'approved':
        return False  # Transfer only if approved

    patient = log.patient
    fhir_data = {
        'patient': create_fhir_patient(patient),
        # Use the correct field name 'created_at' instead of 'date'
        'diagnosis': list(patient.diagnosisrecord_set.all().values('diagnosis', 'created_at')),
        'treatment': list(patient.treatmentplan_set.all().values('treatment_details', 'created_at')),
        'medication': list(patient.medicationrecord_set.all().values('drug_name', 'dosage', 'created_at'))
    }

    success = send_patient_data_to_hospital(destination_hospital_api_url, fhir_data)

    if success:
        update_data_exchange_log(log_id, 'transferred')
        return True
    return False
