from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http import HttpRequest, Http404

from .serializers import AttributeValueSerializer, CatalogSerializer
from .models import AttributeValue, Catalog

from typing import Optional, Union

import json


class ImportCreateView(APIView):
    parser_classes = [JSONParser]

    def post(self, request: HttpRequest, format: Optional[str] = None) -> None:
        """
        Handle POST request to import and create new AttributeValue and Catalog objects.
        """
        for item in request.data:
            key = list(item.keys())[0]

            if key == "AttributeValue":
                # Check if the necessary fields are present in the AttributeValue data
                if (
                    all(k in item[key] for k in ("id", "hodnota"))
                    and len(item[key]) == 2
                ):
                    serializer = AttributeValueSerializer(data=item[key])
                    if serializer.is_valid():
                        serializer.save()

            if key == "Catalog":
                # Check if the necessary fields are present in the Catalog data
                if all(k in item[key] for k in ("id", "nazev")) and len(item[key]) in [
                    2,
                    3,
                ]:
                    catalog_data = item[key]
                    if "products_ids" in catalog_data:
                        if isinstance(catalog_data["products_ids"], list):
                            catalog_data["products_ids"] = json.dumps(
                                catalog_data["products_ids"]
                            )
                        else:
                            catalog_data["products_ids"] = None
                    serializer = CatalogSerializer(data=catalog_data)
                    if serializer.is_valid():
                        serializer.save()

        return Response({"received data": request.data})


class DynamicModelListView(generics.ListAPIView):
    def get_queryset(self) -> Union[list, Http404]:
        model_name = self.kwargs["model_name"]
        if model_name == "catalog":
            return Catalog.objects.all()
        elif model_name == "attribute_value":
            return AttributeValue.objects.all()
        else:
            raise Http404

    def get_serializer_class(self) -> Union[list, Http404]:
        model_name = self.kwargs["model_name"]
        if model_name == "catalog":
            return CatalogSerializer
        elif model_name == "attribute_value":
            return AttributeValueSerializer
        else:
            raise Http404


class DynamicModelDetailView(generics.RetrieveAPIView):
    def get_queryset(self) -> Union[list, Http404]:
        model_name = self.kwargs["model_name"]
        if model_name == "catalog":
            return Catalog.objects.all()
        elif model_name == "attribute_value":
            return AttributeValue.objects.all()
        else:
            raise Http404

    def get_serializer_class(self) -> Union[list, Http404]:
        model_name = self.kwargs["model_name"]
        if model_name == "catalog":
            return CatalogSerializer
        elif model_name == "attribute_value":
            return AttributeValueSerializer
        else:
            raise Http404
