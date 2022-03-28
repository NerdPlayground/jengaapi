from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from identification.serializers import IdentificationSerializer

class IdentificationAPIView(GenericAPIView):
    serializer_class= IdentificationSerializer

    def post(self,request):
        data= request.data
        serializer= IdentificationSerializer(data=data)
        if serializer.is_valid():
            document_type= data.get('documentType')
            first_name= data.get('firstName')
            last_name= data.get('lastName')
            date_of_birth= data.get('dateOfBirth')
            document_number= data.get('documentNumber')
            country_code= data.get('countryCode')

            identification={
                "identity": {
                    "customer": {
                        "fullName": "John Doe ",
                        "firstName": "John",
                        "middlename": "",
                        "lastName": "Doe",
                        "ShortName": "John",
                        "birthDate": "1900-01-01T00:00:00",
                        "birthCityName": "",
                        "deathDate": "",
                        "gender": "",
                        "faceImage": "/9j/4AAQSkZJRgABAAEAYABgA+H8qr6n4e1O71SGFbV/sEOF3O6/N/eb71d/FGkaBVXaq9KfRRRRRUMsKSIdyr0r/9k=",
                        "occupation": "",
                        "nationality": "Refugee"
                    },
                    "documentType": "ALIEN ID",
                    "documentNumber": "654321",
                    "documentSerialNumber": "100500425",
                    "documentIssueDate": "2002-11-29T12:00:00",
                    "documentExpirationDate": "2004-11-28T12:00:00",
                    "IssuedBy": "REPUBLIC OF KENYA",
                    "additionalIdentityDetails": [
                        {
                            "documentNumber": "",
                            "documentType": "",
                            "issuedBy": ""
                        }
                    ],
                    "address": {
                        "provinceName": " ",
                        "districtName": "",
                        "locationName": "",
                        "subLocationName": "",
                        "villageName": ""
                    }
                }
            }
            return Response(identification,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)