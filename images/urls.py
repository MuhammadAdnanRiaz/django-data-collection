from django.urls import path,include
from rest_framework import routers, urlpatterns
from .views import ImageViewSet

router = routers.DefaultRouter()
router.register('',ImageViewSet,basename="images")
urlpatterns = [
    path('',include(router.urls))
]