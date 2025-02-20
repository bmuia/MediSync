from rest_framework import serializers
from .models import CustomUser, Hospital
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'role', 'hospital']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        #Hide sensitive data from non-admins i.e patienys
        if instance.role != 'admin':
            data.pop('hospital')  # Hide hospital field

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









        