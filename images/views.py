from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ImageSerializer
from .models import Images

# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Images.objects.all()
