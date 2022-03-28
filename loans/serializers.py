from rest_framework import serializers

class CreditScoreSerializer(serializers.Serializer):
    countryCode= serializers.CharField()
    creditBureauCode= serializers.CharField()
    customerID= serializers.CharField()
    firstName= serializers.CharField()
    lastName= serializers.CharField()
    nationalId= serializers.CharField()
    reportReason= serializers.CharField()
    reference= serializers.CharField()
    {
        "crbIdentity": {
            "countryCode": "KE",
            "creditBureauCode": "METROPOL_KE",
            "customerID": "99100003500",
            "firstName": "AHMED",
            "lastName": "AHMED",
            "nationalId": "25915141",
            "reportReason": "c",
            "reference": "abc01"
        }
    }