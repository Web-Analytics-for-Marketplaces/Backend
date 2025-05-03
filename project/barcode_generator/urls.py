from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BarcodeViewSet

router = DefaultRouter()
router.register('barcodes', BarcodeViewSet)

urlpatterns = [path('', include(router.urls))]