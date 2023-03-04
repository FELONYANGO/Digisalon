from django.urls import path
from . import views

urlpatterns = [
    path('', views.salon, name='salon'),
    path('signup/', views.signup_view, name='signup_view'),
    path('password_reset/', views.password_reset_view, name='password_reset_view'),
]
