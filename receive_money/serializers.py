from weakref import ref
from rest_framework import serializers

class BillPayMentsSerializer(serializers.Serializer):
    billerCode= serializers.CharField()
    countryCode= serializers.CharField()
    billReference= serializers.CharField()
    amount= serializers.CharField()
    currency= serializers.CharField()
    name= serializers.CharField()
    account= serializers.CharField()
    reference= serializers.CharField()
    mobileNumber= serializers.CharField()
    partnerId= serializers.CharField()

class MerchantPaymentsSerializer(serializers.Serializer):
    till= serializers.CharField()
    paymentRef= serializers.CharField()
    amount= serializers.CharField()
    currency= serializers.CharField()
    id= serializers.CharField()
    partnerRef= serializers.CharField()
    
class BillValidationSerializer(serializers.Serializer):
    billerCode= serializers.CharField()
    customerRefNumber= serializers.CharField()
    amount= serializers.CharField()
    amountCurrency= serializers.CharField()