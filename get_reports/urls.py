from django.urls import path,include
from rest_framework import  urlpatterns
from . import views


urlpatterns = [
    path('',views.get_all_report,name="index"),
    path('<int:vehicle>',views.get_report_for_vehicle),
    path('<int:vehicle>/<date>',views.get_report_for_vehicle_by_date)
]