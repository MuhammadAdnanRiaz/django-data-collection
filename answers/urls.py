from django.urls import path,include
from rest_framework import routers, urlpatterns
from .views import get_answers

router = routers.DefaultRouter()
router.register('',get_answers,basename="answers")
urlpatterns = [
    path('',include(router.urls))
]