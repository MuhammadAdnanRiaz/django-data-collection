from rest_framework import viewsets
from .serializers import AnswersSerializer
from .models import Answers
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class get_answers(viewsets.ModelViewSet):
    serializer_class = AnswersSerializer
    queryset = Answers.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at','updated_at','question']

