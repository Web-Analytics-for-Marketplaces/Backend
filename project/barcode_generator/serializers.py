from rest_framework import serializers
from .models import Barcode

class BarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = ['id','product','code_type','data','image','created_at']