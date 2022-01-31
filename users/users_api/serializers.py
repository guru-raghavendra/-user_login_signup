from email.policy import default
from rest_framework import serializers
from .models import userDetails

class detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = userDetails
        fields = ('__all__')

class loginSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length = 20, default='')
    email=serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=50)
    class Meta:
        model = userDetails
        fields = ('__all__')