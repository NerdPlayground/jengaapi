from django.urls import path
from account_services.views import (
    AccountFullStatementAPIView,
    OpeningAndClosingAccountBalanceAPIVew,
)

urlpatterns= [
    path(
        'account-full-statement/',
        AccountFullStatementAPIView.as_view(),
        name='account-full-statement'
    ),
    path(
        'opening-closing-balance/',
        OpeningAndClosingAccountBalanceAPIVew.as_view(),
        name='opening-closing-balance'
    ),
]