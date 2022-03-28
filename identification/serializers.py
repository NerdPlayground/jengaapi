from rest_framework import serializers

class IdentificationSerializer(serializers.Serializer):
    documentType= serializers.CharField()
    firstName= serializers.CharField()
    lastName= serializers.CharField()
    dateOfBirth= serializers.DateField()
    documentNumber= serializers.CharField()
    countryCode= serializers.CharField()