from rest_framework import serializers
from .models import kisiler

class KisilerSerializer(serializers.ModelSerializer):
    class Meta:
        model=kisiler
        fields='__all__'
        
        