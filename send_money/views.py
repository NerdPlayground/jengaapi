from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from send_money.serializers import (
    RTGSSerializer, SWIFTSerializer,
    PesaLinkToBankSerializer, PesaLinkToMobileSerializer,
    WithinEquityBankSerializer, ToMobileWalletsSerializer,
)


class WithinEquityBankAPIView(GenericAPIView):
    serializer_class = WithinEquityBankSerializer

    def post(self, request):
        data = request.data
        serializer = WithinEquityBankSerializer(data=data)
        if serializer.is_valid():
            source_country_code = data.get('sourceCountryCode')
            source_name = data.get('sourceName')
            source_account_number = data.get('sourceAccountNumber')
            destination_type = data.get('destinationType')
            destination_country_code = data.get('destinationCountryCode')
            destination_name = data.get('destinationName')
            destination_Account_Number = data.get('destinationAccountNumber')
            transfer_type = data.get('transferType')
            amount = data.get('amount')
            currency_code = data.get('currencyCode')
            reference = data.get('reference')
            date = data.get('date')
            description = data.get('description')

            within_equity_bank = {
                "transactionId": "1452854",
                "status": "SUCCESS"
            }
            return Response(within_equity_bank, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToMobileWalletsAPIView(GenericAPIView):
    serializer_class = ToMobileWalletsSerializer

    def post(self, request):
        data = request.data
        serializer = ToMobileWalletsSerializer(data=data)
        if serializer.is_valid():
            source_country_code = data.get('sourceCountryCode')
            source_name = data.get('sourceName')
            source_account_number = data.get('sourceAccountNumber')
            destination_type = data.get('destinationType')
            destination_country_code = data.get('destinationCountryCode')
            destination_name = data.get('destinationName')
            mobile_number= data.get('mobileNumber')
            wallet_name= data.get('walletName')
            transfer_type= data.get('transferType')
            amount= data.get('amount')
            currency_code= data.get('currencyCode')
            date= data.get('date')
            description= data.get('description')

            to_mobile_wallets={
                "transactionId": "",
                "status": "SUCCESS"
            }
            return Response(to_mobile_wallets,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RTGSAPIView(GenericAPIView):
    serializer_class = RTGSSerializer

    def post(self, request):
        data = request.data
        serializer = RTGSSerializer(data=data)
        if serializer.is_valid():
            source_country_code = data.get('sourceCountryCode')
            source_name = data.get('sourceName')
            source_account_number = data.get('sourceAccountNumber')
            destination_type = data.get('destinationType')
            destination_country_code = data.get('destinationCountryCode')
            destination_name = data.get('destinationName')
            bank_code= data.get('bankCode')
            destination_Account_Number = data.get('destinationAccountNumber')
            transfer_type = data.get('transferType')
            amount = data.get('amount')
            currency_code = data.get('currencyCode')
            reference = data.get('reference')
            date = data.get('date')
            description = data.get('description')

            rtgs={
                "transactionId": "000000403777",
                "status": "SUCCESS"
            }
            return Response(rtgs,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SWIFTAPIView(GenericAPIView):
    serializer_class = SWIFTSerializer

    def post(self, request):
        data = request.data
        serializer = SWIFTSerializer(data=data)
        if serializer.is_valid():
            source_country_code = data.get('sourceCountryCode')
            source_name = data.get('sourceName')
            source_account_number = data.get('sourceAccountNumber')
            destination_type = data.get('destinationType')
            destination_country_code = data.get('destinationCountryCode')
            destination_name = data.get('destinationName')
            bank_bic= data.get('bankBic')
            destination_account_number= data.get('destinationAccountNumber')
            address_line_1= data.get('addressline1')
            transfer_type = data.get('transferType')
            amount = data.get('amount')
            currency_code = data.get('currencyCode')
            reference = data.get('reference')
            date = data.get('date')
            description = data.get('description')
            charge_option= data.get('chargeOption')

            swift={
                "transactionId": "000000403794",
                "status": "SUCCESS"
            }
            return Response(swift,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PesaLinkToBankAPIView(GenericAPIView):
    serializer_class = PesaLinkToBankSerializer

    def post(self, request):
        data = request.data
        serializer = PesaLinkToBankSerializer(data=data)
        if serializer.is_valid():
            source_country_code = data.get('sourceCountryCode')
            source_name = data.get('sourceName')
            source_account_number = data.get('sourceAccountNumber')
            destination_type = data.get('destinationType')
            destination_country_code = data.get('destinationCountryCode')
            destination_name = data.get('destinationName')
            mobile_number= data.get('mobileNumber')
            bank_code= data.get('bankCode')
            destination_account_number= data.get('destinationAccountNumber')
            transfer_type = data.get('transferType')
            amount = data.get('amount')
            currency_code = data.get('currencyCode')
            reference = data.get('reference')
            date = data.get('date')
            description = data.get('description')

            pesa_link_bank={
                "transactionId": "10000345333355",
                "status": "SUCCESS",
                "description": "Confirmed. Ksh 100 Sent to 01100762802910 -Tom Doe from your account 1460163242696 on 20-05-2019 at 141313 Ref. 707700078800 Thank you"
            }
            return Response(pesa_link_bank,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PesaLinkToMobileAPIView(GenericAPIView):
    serializer_class = PesaLinkToMobileSerializer

    def post(self, request):
        data = request.data
        serializer = PesaLinkToMobileSerializer(data=data)
        if serializer.is_valid():
            source_country_code = data.get('sourceCountryCode')
            source_name = data.get('sourceName')
            source_account_number = data.get('sourceAccountNumber')
            destination_type = data.get('destinationType')
            destination_country_code = data.get('destinationCountryCode')
            destination_name = data.get('destinationName')
            mobile_number= data.get('mobileNumber')
            bank_code= data.get('bankCode')
            transfer_type = data.get('transferType')
            amount = data.get('amount')
            currency_code = data.get('currencyCode')
            reference = data.get('reference')
            date = data.get('date')
            
            pesa_link_mobile={
                "transactionId": "10000345333355",
                "status": "SUCCESS"
            }
            return Response(pesa_link_mobile,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
