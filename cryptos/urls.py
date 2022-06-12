from django.urls import path
from . import views

urlpatterns = [
    path('api/token/', views.api_get_token),
    path('api/cryptos/', views.api_get_cryptos),
    path('api/register/', views.api_register),
]