from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AttributeValueSerializer, CatalogSerializer
import json


class AttributeValueCreateView(APIView):
    parser_classes = [JSONParser]

    def post(self, request, format=None) -> None:
        for item in request.data:
            key = list(item.keys())[0]

            if key == "AttributeValue":
                serializer = AttributeValueSerializer(data=item[key])
                if serializer.is_valid():
                    serializer.save()

            if key == "Catalog":
                print(f"Data je {item[key]}")
                catalog_data = item[key]
                if "products_ids" in catalog_data:
                    catalog_data["products_ids"] = json.dumps(
                        catalog_data["products_ids"]
                    )
                serializer = CatalogSerializer(data=item[key])
                if serializer.is_valid():
                    serializer.save()

        return Response({"received data": request.data})
