from django.db import models
from inventory.models import Product

class Barcode(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    code_type = models.CharField(max_length=32)
    data = models.CharField(max_length=255)
    image = models.ImageField(upload_to='barcodes/')
    created_at = models.DateTimeField(auto_now_add=True)