from django.urls import path
from receive_money.views import (
    BillPayMentsAPIView,
    MerchantPaymentsAPIView,
    BillValidationAPIView
)

urlpatterns= [
    path('receive-payments/bill-payments/',BillPayMentsAPIView.as_view(),name='bill-payments'),
    path('receive-payments/merchant-payments/',MerchantPaymentsAPIView.as_view(),name='merchant-payments'),
    path('receive-payments/bill-validation/',BillValidationAPIView.as_view(),name='bill-validation'),
]