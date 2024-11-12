from hashlib import sha3_256
from rest_framework import serializers, authentication
from .models import *
from django.contrib.auth.models import User

class SkoolSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user', read_only=True)

    class Meta:
        model = Skool
        fields = ('pk','user_name','image', 'designationEcole', 'arreteMin', 'adresse', 'telephone', 'email', 'typesEcole','promoteur', 'biographie')

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('pk','username','password', 'email')

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'


class DegreeSerializer(serializers.ModelSerializer):
    
    class Meta:
        read_only_fields = ['skool']
        model = Degree
        fields = ('pk','skool','designation')
        
        

class MasomoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('pk','degree','option','classe')
        
