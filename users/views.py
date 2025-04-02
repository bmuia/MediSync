from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import IsDoctor, IsNurse, IsAdmin, IsPatient, IsDataAnalyst,IsLabTechnician,IsPharmacist,IsPublicHealthOfficial,IsRadiologist
from .serializers import RegistrationSerializer, HospitalSerializer
from .models import CustomUser, Hospital
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Views for different user roles
class DoctorOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request):
        return Response({"message": "Hello Doctor, you have access!"})


class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Hello Admin, you have access!"})


class NurseOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsNurse]

    def get(self, request):
        return Response({"message": "Hello Nurse, you have access!"})


class PatientOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsPatient]

    def get(self, request):
        return Response({"message": "Hello Patient, you have access!"})

class RadiologistOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsRadiologist]

    def get(self, request):
        return Response({"message": "Hello Radiologist, you have access!"})

class LabTechnicianOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsLabTechnician]

    def get(self, request):
        return Response({"message": "Hello Lab Technician, you have access!"})

class PharmacistOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsPharmacist]

    def get(self, request):
        return Response({"message": "Hello Pharmacist, you have access!"})

class DataAnalystOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsDataAnalyst]

    def get(self, request):
        return Response({"message": "Hello Data Analyst, you have access!"})

class PublicHealthOfficialOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsPublicHealthOfficial]

    def get(self, request):
        return Response({"message": "Hello Public Health Official, you have access!"})


# Registration view
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def create(self, request, *args, **kwargs):
        if request.user.role != 'admin':  
            return Response({"error": "Only admins can register new users."}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        role = serializer.validated_data.get("role", "patient")  # Default role: patient
        if role not in dict(CustomUser.ROLE_CHOICES).keys():
            return Response({"error": "Invalid role."}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        response_data = {
            "email": user.email,
            "role": user.role,  
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customize JWT response to include user role."""
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['role'] = self.user.role
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    """Customize Login view to return token and role."""
    serializer_class = CustomTokenObtainPairSerializer


class HospitalAPIView(generics.ListAPIView):
    """List the hospitals"""
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class HospitalCreateAPIView(generics.CreateAPIView): 
    """Create a hospital"""
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [ IsAuthenticated,IsAdmin]

class HospitalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update, or delete a hospital by ID"""
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [ IsAuthenticated,IsAdmin]
