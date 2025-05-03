from rest_framework import serializers
from .models import Product, Stock

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','sku','name','description','price']

class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)
    class Meta:
        model = Stock
        fields = ['id','product','product_id','quantity','updated_at']