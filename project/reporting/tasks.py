from celery import shared_task
from .models import Report
from django.utils import timezone

@shared_task
def generate_report(report_id):
    report = Report.objects.get(pk=report_id)
    report.run()
    report.generated_at = timezone.now()
    report.save()