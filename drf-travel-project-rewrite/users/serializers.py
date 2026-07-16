from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    
    def create(self, validation_data):
        user = User.objects.create_user(
            username = validation_data['username'],
            email = validation_data['email'],
            password = validation_data['password']
        )

        return user