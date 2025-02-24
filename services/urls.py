from django.urls import path
from .views import ServiceRequestListCreateView, ServiceRequestDetailView

urlpatterns = [
    path("api/requests/", ServiceRequestListCreateView.as_view(), name="service_request_list"),
    path("api/requests/<int:pk>/", ServiceRequestDetailView.as_view(), name="service_request_detail"),
]
