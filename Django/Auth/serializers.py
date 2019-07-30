from rest_framework import serializers
from Auth.models import Auth

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('id', 'user_name', 'password', 'createdAt', 'updatedAt')