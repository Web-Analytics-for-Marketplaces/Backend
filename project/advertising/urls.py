from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampaignViewSet, AdMetricViewSet

router = DefaultRouter()
router.register('campaigns', CampaignViewSet)
router.register('metrics', AdMetricViewSet)

urlpatterns = [path('', include(router.urls))]