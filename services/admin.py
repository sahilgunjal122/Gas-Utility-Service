from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ("customer", "service_type", "status", "created_at")
    list_filter = ("status", "service_type")
    search_fields = ("customer__username", "service_type")
    ordering = ("-created_at",)
    list_editable = ("status",)
