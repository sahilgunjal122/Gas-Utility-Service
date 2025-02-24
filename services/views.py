from rest_framework import generics, permissions
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

class ServiceRequestListCreateView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class ServiceRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]


