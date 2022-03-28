from django.urls import path
from loans.views import CreditScoreAPIView

urlpatterns= [
    path('loans/credit-score/',CreditScoreAPIView.as_view(),name='credit-score'),
]