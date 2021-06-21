from rest_framework import viewsets
from .serializers import ChecklistSerializer
from .models import Checklist
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class Checklist(viewsets.ModelViewSet):
    serializer_class = ChecklistSerializer
    queryset = Checklist.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['image']

