from rest_framework import serializers

class AccountFullStatementSerializer(serializers.Serializer):
    countryCode= serializers.CharField()
    accountNumber= serializers.CharField()
    fromDate= serializers.DateField()
    toDate= serializers.DateField()
    limit= serializers.IntegerField()
    reference= serializers.CharField()
    serial= serializers.CharField()
    postedDateTime= serializers.CharField()
    date= serializers.CharField()
    currency= serializers.CharField()
    amount= serializers.IntegerField()

class OpeningAndClosingAccountBalanceSerializer(serializers.Serializer):
    countryCode= serializers.CharField()
    accountId= serializers.CharField()
    date= serializers.DateField()