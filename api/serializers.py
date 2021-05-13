from rest_framework import serializers
from django_test import models

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Register
        fields='__all__'



