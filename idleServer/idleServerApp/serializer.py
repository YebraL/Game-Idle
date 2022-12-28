from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=AppUser
        fields = ['id', 'email', 'username', 'created', 'first_name', 'last_name']
