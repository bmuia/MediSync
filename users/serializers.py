from rest_framework import serializers
from .models import CustomUser, Hospital
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer()  # If you want to show hospital details for any user
    first_name = serializers.CharField()  # Assuming you have first_name in CustomUser
    last_name = serializers.CharField()   # Assuming you have last_name in CustomUser

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'role', 'hospital', 'first_name', 'last_name']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Hide sensitive data for non-admins (i.e., patients)
        if instance.role != 'admin':
            data.pop('hospital')  # Hide hospital field for non-admin users
        if instance.role != 'doctor':
            data.pop('first_name')  # Hide doctor-specific data for non-doctors
            data.pop('last_name')

        return data


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'role', 'hospital']

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            role=validated_data['role'],
            hospital=validated_data.get('hospital', None),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user









        