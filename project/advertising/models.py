from django.db import models
from inventory.models import Product

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

class AdMetric(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    spend = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)