from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import IsDoctor, IsNurse, IsAdmin, IsPatient
from .serializers import RegistrationSerializer
from .models import CustomUser

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


# Registration view
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
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

