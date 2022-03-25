from rest_framework import serializers


class WithinEquityBankSerializer(serializers.Serializer):
    sourceCountryCode = serializers.CharField()
    sourceName = serializers.CharField()
    sourceAccountNumber = serializers.CharField()
    destinationType = serializers.CharField()
    destinationCountryCode = serializers.CharField()
    destinationName = serializers.CharField()
    destinationAccountNumber = serializers.CharField()
    transferType = serializers.CharField()
    amount = serializers.IntegerField(),
    currencyCode = serializers.CharField()
    reference = serializers.CharField()
    date = serializers.DateField()
    description = serializers.CharField()

class ToMobileWalletsSerializer(serializers.Serializer):
    sourceCountryCode = serializers.CharField()
    sourceName = serializers.CharField()
    sourceAccountNumber = serializers.CharField()
    destinationType = serializers.CharField()
    destinationCountryCode = serializers.CharField()
    destinationName = serializers.CharField()
    mobileNumber= serializers.CharField()
    walletName= serializers.CharField()
    transferType = serializers.CharField()
    amount = serializers.IntegerField(),
    currencyCode = serializers.CharField()
    date = serializers.DateField()
    description = serializers.CharField()

class RTGSSerializer(serializers.Serializer):
    sourceCountryCode = serializers.CharField()
    sourceName = serializers.CharField()
    sourceAccountNumber = serializers.CharField()
    destinationType = serializers.CharField()
    destinationCountryCode = serializers.CharField()
    destinationName = serializers.CharField()
    bankCode = serializers.CharField()
    destinationAccountNumber = serializers.CharField()
    transferType = serializers.CharField()
    amount = serializers.IntegerField(),
    currencyCode = serializers.CharField()
    reference = serializers.CharField()
    date = serializers.DateField()
    description = serializers.CharField()

class SWIFTSerializer(serializers.Serializer):
    sourceCountryCode = serializers.CharField()
    sourceName = serializers.CharField()
    sourceAccountNumber = serializers.CharField()
    destinationType = serializers.CharField()
    destinationCountryCode = serializers.CharField()
    destinationName = serializers.CharField()
    bankBic = serializers.CharField()
    destinationAccountNumber = serializers.CharField()
    addressline1 = serializers.CharField()
    transferType = serializers.CharField()
    amount = serializers.IntegerField(),
    currencyCode = serializers.CharField()
    reference = serializers.CharField()
    date = serializers.DateField()
    description = serializers.CharField()
    chargeOption = serializers.CharField()
    
class PesaLinkToBankSerializer(serializers.Serializer):
    sourceCountryCode = serializers.CharField()
    sourceName = serializers.CharField()
    sourceAccountNumber = serializers.CharField()
    destinationType = serializers.CharField()
    destinationCountryCode = serializers.CharField()
    destinationName = serializers.CharField()
    mobileNumber= serializers.CharField()
    bankCode = serializers.CharField()
    destinationAccountNumber = serializers.CharField()
    transferType = serializers.CharField()
    amount = serializers.IntegerField(),
    currencyCode = serializers.CharField()
    reference = serializers.CharField()
    date = serializers.DateField()
    description = serializers.CharField()

class PesaLinkToMobileSerializer(serializers.Serializer):
    sourceCountryCode = serializers.CharField()
    sourceName = serializers.CharField()
    sourceAccountNumber = serializers.CharField()
    destinationType = serializers.CharField()
    destinationCountryCode = serializers.CharField()
    destinationName = serializers.CharField()
    bankCode = serializers.CharField()
    mobileNumber= serializers.CharField()
    transferType = serializers.CharField()
    amount = serializers.IntegerField(),
    currencyCode = serializers.CharField()
    reference = serializers.CharField()
    date = serializers.DateField()