from rest_framework import serializers

class ForexRatesSerializer(serializers.Serializer):
    countryCode= serializers.CharField()
    currencyCode= serializers.CharField()
    amount= serializers.IntegerField()
    toCurrency= serializers.CharField()
    accountNumber= serializers.CharField()