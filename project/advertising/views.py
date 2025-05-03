from rest_framework import viewsets
from .models import Campaign, AdMetric
from .serializers import CampaignSerializer, AdMetricSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class AdMetricViewSet(viewsets.ModelViewSet):
    queryset = AdMetric.objects.all()
    serializer_class = AdMetricSerializer