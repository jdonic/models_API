from rest_framework import serializers

from .models import AttributeValue, Catalog

import json


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ("id", "hodnota")


class CatalogSerializer(serializers.ModelSerializer):
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
