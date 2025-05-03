from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/inventory/', include('inventory.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('api/ads/', include('advertising.urls')),
    path('api/barcode/', include('barcode_generator.urls')),
    path('api/reporting/', include('reporting.urls')),
]