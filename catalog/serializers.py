from rest_framework import serializers

from .models import AttributeValue, Catalog


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ("id", "hodnota")


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ("id", "nazev", "products_ids")
