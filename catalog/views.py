from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http import HttpRequest

from .serializers import AttributeValueSerializer, CatalogSerializer
from .models import AttributeValue, Catalog

from typing import Optional

import json


class ImportCreateView(APIView):
    parser_classes = [JSONParser]

    def post(self, request: HttpRequest, format: Optional[str] = None) -> None:
        for item in request.data:
            key = list(item.keys())[0]

            if key == "AttributeValue":
                if (
                    all(k in item[key] for k in ("id", "hodnota"))
                    and len(item[key]) == 2
                ):
                    serializer = AttributeValueSerializer(data=item[key])
                    if serializer.is_valid():
                        serializer.save()

            if key == "Catalog":
                if all(k in item[key] for k in ("id", "nazev")) and len(item[key]) in [
                    2,
                    3,
                ]:
                    catalog_data = item[key]
                    if "products_ids" in catalog_data:
                        catalog_data["products_ids"] = json.dumps(
                            catalog_data["products_ids"]
                        )
                    serializer = CatalogSerializer(data=item[key])
                    if serializer.is_valid():
                        serializer.save()

        return Response({"received data": request.data})


class AttributeValueListView(generics.ListAPIView):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer


class AttributeValueDetailView(generics.RetrieveAPIView):
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer


class CatalogListView(generics.ListAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class CatalogDetailView(generics.RetrieveAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
