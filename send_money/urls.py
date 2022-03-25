from django.urls import path
from send_money.views import (
    RTGSAPIView,SWIFTAPIView,
    PesaLinkToBankAPIView,PesaLinkToMobileAPIView,
    WithinEquityBankAPIView,ToMobileWalletsAPIView,
)

urlpatterns= [
    path('send-money/rtgs/',RTGSAPIView.as_view(),name='rtgs'),
    path('send-money/swift/',SWIFTAPIView.as_view(),name='swift'),
    path('send-money/pesa-link-mobile/',PesaLinkToMobileAPIView.as_view(),name='pesa-link-mobile'),
    path('send-money/pesa-link-bank/',PesaLinkToBankAPIView.as_view(),name='pesa-link-bank'),
    path('send-money/within-equity-bank/',WithinEquityBankAPIView.as_view(),name='within-equity-bank'),
    path('send-money/to-mobile-wallets/',ToMobileWalletsAPIView.as_view(),name='to-mobile-wallets'),
]