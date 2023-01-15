from django.db import models


class AttributeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    hodnota = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.hodnota


class Catalog(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=255)
    products_ids = models.JSONField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nazev
