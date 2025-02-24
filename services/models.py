from django.conf import settings
from django.db import models

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ("gas_leak", "Gas Leak"),
        ("meter_issue", "Meter Issue"),
        ("billing", "Billing Issue"),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="service_requests"
    )
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    description = models.TextField()
    status = models.CharField(max_length=20, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} - {self.status}"
