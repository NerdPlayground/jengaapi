from django.urls import path
from identification.views import IdentificationAPIView

urlpatterns= [
    path('search-verify-identification/',IdentificationAPIView.as_view(),name='search-verify-identification')
]