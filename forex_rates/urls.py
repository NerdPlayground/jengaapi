from django.urls import path
from forex_rates.views import ForexRatesAPIView

urlpatterns= [
    path('forex-rates/',ForexRatesAPIView.as_view(),name='forex-rates'),
]