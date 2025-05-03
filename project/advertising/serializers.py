from rest_framework import serializers
from .models import Campaign, AdMetric

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id','name','products','budget','start_date','end_date']

class AdMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdMetric
        fields = ['id','campaign','impressions','clicks','spend','created_at']