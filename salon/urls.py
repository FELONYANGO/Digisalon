from django.urls import path
from . import views

urlpatterns = [
    path('', views.salon, name='salon'),
]
