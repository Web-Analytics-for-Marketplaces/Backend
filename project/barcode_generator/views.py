from rest_framework import viewsets
from .models import Barcode
from .serializers import BarcodeSerializer

class BarcodeViewSet(viewsets.ModelViewSet):
    queryset = Barcode.objects.all()
    serializer_class = BarcodeSerializer