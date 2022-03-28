from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from loans.serializers import CreditScoreSerializer

class CreditScoreAPIView(GenericAPIView):
    serializer_class = CreditScoreSerializer

    def post(self,request):
        data= request.data
        serializer= CreditScoreSerializer(data=data)
        if serializer.is_valid():
            country_code= data.get('countryCode')
            credit_bureau_code= data.get('creditBureauCode')
            customer_id= data.get('customerID')
            first_name= data.get('firstName')
            last_name= data.get('lastName')
            national_id= data.get('nationalId')
            report_reason= data.get('reportReason')
            reference= data.get('reference')

            credit_score={
                "Person": {
                    "PersonName": {},
                    "IdentityDocument": {
                        "IdentityDocumentID": "1234568",
                        "IdentityDocumentType": "National ID"
                    }
                },
                "CreditAccountsSummary":[
                    {
                        "AccountIdentifier": {
                            "AccountID": "0011547896523",
                            "AccountCurrency": {}
                        },
                        "AccountType": "36",
                        "AccountOpenDate": "17012014",
                        "AccountOwnership": "true",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "65000.00000",
                            "65000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "5000.00000",
                        "LastPaymentReceivedDate": "20062014",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "30062014",
                        "AccountStatus": "F",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "0011547896523",
                            "AccountCurrency": {}
                        },
                        "AccountType": "09",
                        "AccountOpenDate": "09062011",
                        "AccountOwnership": "true",
                        "Balance": "106458.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "200000.00000",
                            "200000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "1667.00000",
                        "LastPaymentReceivedDate": "15062018",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "30062018",
                        "AccountStatus": "W",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "0011547896523",
                            "AccountCurrency": {}
                        },
                        "AccountType": "36",
                        "AccountOpenDate": "14052014",
                        "AccountOwnership": "true",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "80000.00000",
                            "80000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "6960.00000",
                        "LastPaymentReceivedDate": "15122014",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31122014",
                        "AccountStatus": "F",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "0011547896523",
                            "AccountCurrency": {}
                        },
                        "AccountType": "36",
                        "AccountOpenDate": "22092014",
                        "AccountOwnership": "true",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "1000.00000",
                            "1000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "1000.00000",
                        "LastPaymentReceivedDate": "15102014",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31102014",
                        "AccountStatus": "F",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "0011547896523",
                            "AccountCurrency": {}
                        },
                        "AccountType": "36",
                        "AccountOpenDate": "29122014",
                        "AccountOwnership": "true",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "80000.00000",
                            "80000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "6666.67000",
                        "LastPaymentReceivedDate": "16032015",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31032015",
                        "AccountStatus": "F",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "0011547896523",
                            "AccountCurrency": {}
                        },
                        "AccountType": "36",
                        "AccountOpenDate": "20032015",
                        "AccountOwnership": "true",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "80000.00000",
                            "80000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "6666.67000",
                        "LastPaymentReceivedDate": "16012016",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31012016",
                        "AccountStatus": "F",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "N:000019:01:2015",
                            "AccountCurrency": {}
                        },
                        "AccountType": "23",
                        "AccountOpenDate": "06012015",
                        "AccountOwnership": "false",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "300000.00000",
                            "300000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "20562.00000",
                        "LastPaymentReceivedDate": "27102017",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31122017",
                        "AccountStatus": "F",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "068-P-12365478",
                            "AccountCurrency": {}
                        },
                        "AccountType": "04",
                        "AccountOpenDate": "13102011",
                        "AccountOwnership": "true",
                        "Balance": "39844.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "40000.00000",
                            "40000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "2500.00000",
                        "LastPaymentReceivedDate": "16072018",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31072018",
                        "AccountStatus": "W",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "068-P-25417854",
                            "AccountCurrency": {}
                        },
                        "AccountType": "04",
                        "AccountOpenDate": "19082015",
                        "AccountOwnership": "true",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "50000.00000",
                            "50000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "2500.00000",
                        "LastPaymentReceivedDate": "13022018",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31072018",
                        "AccountStatus": "F",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "0011547896523",
                            "AccountCurrency": {}
                        },
                        "AccountType": "23",
                        "AccountOpenDate": "02022016",
                        "AccountOwnership": "true",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "80000.00000",
                            "80000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "6666.67000",
                        "LastPaymentReceivedDate": "16122016",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31012017",
                        "AccountStatus": "F",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "2569774",
                            "AccountCurrency": {}
                        },
                        "AccountType": "12",
                        "AccountOpenDate": "02062016",
                        "AccountOwnership": "false",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "3000.00000",
                            "3000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "3726.00000",
                        "LastPaymentReceivedDate": "26122016",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "30062018",
                        "AccountStatus": "F",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "11110571749286",
                            "AccountCurrency": {}
                        },
                        "AccountType": "23",
                        "AccountOpenDate": "14022017",
                        "AccountOwnership": "true",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "120000.00000",
                            "120000.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "10000.00000",
                        "LastPaymentReceivedDate": "15112017",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31122017",
                        "AccountStatus": "F",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "JKCBDL1724301111",
                            "AccountCurrency": {}
                        },
                        "AccountType": "12",
                        "AccountOpenDate": "30082017",
                        "AccountOwnership": "false",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "5400.00000",
                            "5400.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "None",
                        "LastPaymentReceivedDate": "None",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "13122017",
                        "AccountStatus": "A",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "BCKMLD1802229762",
                            "AccountCurrency": {}
                        },
                        "AccountType": "12",
                        "AccountOpenDate": "08042018",
                        "AccountOwnership": "false",
                        "Balance": "0.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "5400.00000",
                            "5400.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "None",
                        "LastPaymentReceivedDate": "11062018",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "21062018",
                        "AccountStatus": "A",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "MKDLCB1814647289",
                            "AccountCurrency": {}
                        },
                        "AccountType": "12",
                        "AccountOpenDate": "26052018",
                        "AccountOwnership": "false",
                        "Balance": "5400.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "5400.00000",
                            "5400.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "5400.00000",
                        "LastPaymentReceivedDate": "26052018",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31052018",
                        "AccountStatus": "W",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "MKCDLB1818039369",
                            "AccountCurrency": {}
                        },
                        "AccountType": "12",
                        "AccountOpenDate": "29062018",
                        "AccountOwnership": "false",
                        "Balance": "2150.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "2150.00000",
                            "2150.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "2150.00000",
                        "LastPaymentReceivedDate": "29062018",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "30062018",
                        "AccountStatus": "W",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    },
                    {
                        "AccountIdentifier": {
                            "AccountID": "MDLBBCK1821123688",
                            "AccountCurrency": {}
                        },
                        "AccountType": "12",
                        "AccountOpenDate": "29072018",
                        "AccountOwnership": "false",
                        "Balance": "2150.00000",
                        "DelinquencyStatus": "No delinquency",
                        "Original_Amount": [
                            "2150.00000",
                            "2150.00000"
                        ],
                        "PastDueAmount": "0.00000",
                        "LastPaymentAmount": "2150.00000",
                        "LastPaymentReceivedDate": "30072018",
                        "NoofDelayed_Payments": "0",
                        "PostedDateTime": "31072018",
                        "AccountStatus": "W",
                        "LoanAccount": {
                            "PastDueDate": {},
                            "LoanHighestDaysInArrears": {}
                        }
                    }
                ],
                "CreditBureau": {
                    "score": "772",
                    "creditApplications90Days": "0",
                    "creditApplications180Days": "0",
                    "creditApplications365Days": "0",
                    "crbEnqiry90Days": "0",
                    "crbEnqiry180Days": "0",
                    "crbEnqiry365Days": "0",
                    "BouncedCheques90Days": "0",
                    "BouncedCheques180Days": "0",
                    "BouncedCheques365Days": "0",
                    "AcctNonPerformingCurrent": "0",
                    "AcctNonPerformingHisto": "0",
                    "AcctPerformingCurrent": "15",
                    "AcctPerformingHisto": "NaN",
                    "IsFraud": "false",
                    "isGuarantor": "false",
                    "delinquency_code": "No delinquency"
                }
            }
            return Response(credit_score,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)