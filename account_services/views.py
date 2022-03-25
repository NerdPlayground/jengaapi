from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from account_services.serializers import (
    AccountFullStatementSerializer,
    OpeningAndClosingAccountBalanceSerializer,
)

class AccountFullStatementAPIView(GenericAPIView):
    serializer_class= AccountFullStatementSerializer

    def post(self,request):
        data= request.data
        serializer= AccountFullStatementSerializer(data=data)
        if serializer.is_valid():
            country_code= data.get('countryCode')
            account_number= data.get('accountNumber')
            from_date= data.get('fromDate')
            to_date= data.get('toDate')
            limit= data.get('limit')
            reference= data.get('reference')
            serial= data.get('serial')
            posted_date_time= data.get('postedDateTime')
            date= data.get('date')
            currency= data.get('currency')
            amount= data.get('amount')

            account_full_Statement={
                "accountNumber": account_number,
                "currency": currency,
                "balance": 997382.57,
                "transactions": [
                    {
                        "reference": reference,
                        "date": "2018-07-13T00:00:00.000",
                        "description": "EQUITEL-BUNDLE/254764555383/8755",
                        "amount": amount,
                        "serial": serial,
                        "postedDateTime": posted_date_time,
                        "type": "Debit",
                        "runningBalance": {
                            "currency": currency,
                            "amount": amount
                        }
                    },
                ]
            }
            return Response(account_full_Statement,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OpeningAndClosingAccountBalanceAPIVew(GenericAPIView):
    serializer_class= OpeningAndClosingAccountBalanceSerializer

    def post(self,request):
        data= request.data
        serializer= OpeningAndClosingAccountBalanceSerializer(data=data)
        
        if serializer.is_valid():
            countryCode= data.get("countryCode")
            accountId= data.get("accountId")
            date= data.get("date")

            opening_closing_account_balance={
                "balances": [
                    {
                        "type": "Closing Balance",
                        "amount": "10810.00"
                    },
                    {
                        "type": "Opening Balance",
                        "amount": "103.00"
                    }
                ]
            }
            return Response(opening_closing_account_balance,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)