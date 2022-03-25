from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from airtime.serializers import PurchaseAirtimeSerializer

class PurchaseAirtimeAPIView(GenericAPIView):
    serializer_class = PurchaseAirtimeSerializer

    def post(self,request):
        data = request.data
        serializer= PurchaseAirtimeSerializer(data=data)
        if serializer.is_valid():
            country_code= data.get('countryCode')
            mobile_number= data.get('mobileNumber')
            amount= data.get('amount')
            reference= data.get('reference')
            telco= data.get('telco')

            purchase_airtime={
                "referenceNumber": "4568899373748",
                "status": "SUCCESS"
            }
            return Response(purchase_airtime,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)