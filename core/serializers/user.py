from rest_framework import serializers
from core.models import User
from datetime import date
from django.contrib.auth.models import Group


class UserWriteSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8,)
    confirm_password = serializers.CharField(write_only=True)
    

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'confirm_password': {'write_only': True},  
        }

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "As senhas não coincidem."})
        return data
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password', None)

        # Cria usuário
        user = User(**validated_data)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return user


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']
