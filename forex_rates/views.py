from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from forex_rates.serializers import ForexRatesSerializer

class ForexRatesAPIView(GenericAPIView):
    serializer= ForexRatesSerializer

    def post(self,request):
        data= request.data
        serializer= ForexRatesSerializer(data=data)
        if serializer.is_valid():
            country_code= data.get('countryCode')
            currency_code= data.get('currencyCode')
            amount= data.get('amount')
            to_currency= data.get('toCurrency')
            account_number= data.get('accountNumber')
            
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)