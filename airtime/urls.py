from django.urls import path
from airtime.views import PurchaseAirtimeAPIView

urlpatterns= [
    path('airtime/purchase-airtime/',PurchaseAirtimeAPIView.as_view(),name='purchase-airtime')
]