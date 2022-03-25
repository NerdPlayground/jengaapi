from rest_framework import serializers

class PurchaseAirtimeSerializer(serializers.Serializer):
    countryCode= serializers.CharField()
    mobileNumber = serializers.CharField()
    amount = serializers.IntegerField()
    reference = serializers.CharField()
    telco = serializers.CharField()
    '''
    {
        "customer": {
            "countryCode": "KE",
            "mobileNumber": "0763000000"
        },
        "airtime": {
            "amount": 100,
            "reference": "692194625798",
            "telco": "Equitel"
        }
    }
    '''