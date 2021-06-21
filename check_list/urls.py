from django.urls import path,include
from rest_framework import routers, urlpatterns
from .views import Checklist

router = routers.DefaultRouter()
router.register('',Checklist,basename="Checklist")
urlpatterns = [
    path('',include(router.urls))
]