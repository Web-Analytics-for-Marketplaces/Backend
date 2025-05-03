from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=255)
    parameters = models.JSONField()
    generated_at = models.DateTimeField(null=True, blank=True)
    result = models.JSONField(null=True, blank=True)

    def run(self):
        # Placeholder aggregation logic
        self.result = {'status': 'completed'}
        self.save()