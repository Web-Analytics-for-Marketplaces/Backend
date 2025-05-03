from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        report = serializer.save()
        from .tasks import generate_report
        generate_report.delay(report.id)