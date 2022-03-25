from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from receive_money.serializers import (
    BillPayMentsSerializer,
    MerchantPaymentsSerializer,
    BillValidationSerializer
)

class BillPayMentsAPIView(GenericAPIView):
    serializer_class= BillPayMentsSerializer

    def post(self,request):
        data= request.data
        serializer= BillPayMentsSerializer(data=data)
        if serializer.is_valid():
            biller_code= data.get('billerCode')
            country_code= data.get('countryCode')
            bill_reference= data.get('billReference')
            amount= data.get('amount')
            currency= data.get('currency')
            name= data.get('name')
            account= data.get('account')
            reference= data.get('reference')
            mobile_number= data.get('mobileNumber')
            partner_id= data.get('partnerId')

            bill_payment={
                "transactionId": "123456729123",
                "status": "SUCCESS"
            }
            return Response(bill_payment,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class MerchantPaymentsAPIView(GenericAPIView):
    serializer_class= MerchantPaymentsSerializer

    def post(self,request):
        data= request.data
        serializer= MerchantPaymentsSerializer(data=data)
        if serializer.is_valid():
            till= data.get('till')
            payment_ref= data.get('paymentRef')
            amount= data.get('amount')
            currency= data.get('currency')
            id= data.get('id')
            partner_ref= data.get('partnerRef')

            merchant_payment={
                "status": "SUCCESS",
                "merchantName": "A N Other",
                "transactionId": "931118931118"
            }
            return Response(merchant_payment,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class BillValidationAPIView(GenericAPIView):
    serializer_class= BillValidationSerializer

    def post(self,request):
        data= request.data
        serializer= BillValidationSerializer(data=data)
        if serializer.is_valid():
            biller_code= data.get('billerCode')
            customer_ref_number= data.get('customerRefNumber')
            amount= data.get('amount')
            amount_currency= data.get('amountCurrency')
            
            bill_validation={
                "bill": {
                    "CustomerRefNumber": "28055948",
                    "amount": "20000",
                    "amountCurrency": "KES",
                    "name": "A N Other",
                    "status": True,
                    "billStatus": "1",
                    "createdOn": "2018-05-21T00:00:00+03:00",
                    "message": "SUCCESS"
                }
            }
            return Response(bill_validation,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)