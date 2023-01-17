from rest_framework import serializers

from .models import AttributeValue, Catalog

import json


class AttributeValueSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = AttributeValue
        fields = ("id", "hodnota")

    def create(self, validated_data: AttributeValue) -> None:
        id = validated_data.get("id")
        instance = AttributeValue.objects.filter(id=id).first()
        if instance:
            for key, value in validated_data.items():
                setattr(instance, key, value)
            instance.save()
            return instance
        return super().create(validated_data)


class CatalogSerializer(serializers.ModelSerializer):
    """
    Converts the Catalog object to its representation in JSON format.
    If the products_ids field is None, it will be removed from the representation.
    Otherwise, it will be converted from a string to a list.
    """

    id = serializers.IntegerField(required=False)

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

    def create(self, validated_data: Catalog) -> None:
        id = validated_data.get("id")
        instance = Catalog.objects.filter(id=id).first()
        if instance:
            for key, value in validated_data.items():
                if key == "products_ids" and value == "None":
                    setattr(instance, key, None)
                else:
                    setattr(instance, key, value)
            instance.save()
            return instance
        return super().create(validated_data)
