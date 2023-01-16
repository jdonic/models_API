from rest_framework import serializers

from .models import AttributeValue, Catalog

import json


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ("id", "hodnota")


class CatalogSerializer(serializers.ModelSerializer):
    """
    Converts the Catalog object to its representation in JSON format.
    If the products_ids field is None, it will be removed from the representation.
    Otherwise, it will be converted from a string to a list.
    """

    class Meta:
        model = Catalog
        fields = ("id", "nazev", "products_ids")

    def to_representation(self, instance: Catalog) -> None:
        rep = super().to_representation(instance)
        if rep["products_ids"] is None:
            del rep["products_ids"]
        else:
            rep["products_ids"] = json.loads(instance.products_ids)
        return rep
