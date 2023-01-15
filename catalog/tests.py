from django.test import TestCase
from rest_framework.test import APIClient
from .models import AttributeValue, Catalog
from .serializers import AttributeValueSerializer, CatalogSerializer


class AttributeValueTestCase(TestCase):
    def setUp(self) -> None:
        AttributeValue.objects.create(id=1, hodnota="test value")

    def test_attribute_value_created(self) -> None:
        attribute_value = AttributeValue.objects.get(id=1)
        self.assertEqual(attribute_value.hodnota, "test value")

    def test_attribute_value_str(self) -> None:
        attribute_value = AttributeValue.objects.get(id=1)
        self.assertEqual(f"{attribute_value}", "test value")


class CatalogTestCase(TestCase):
    def setUp(self) -> None:
        Catalog.objects.create(id=1, nazev="test catalog", products_ids=[1, 2, 3])

    def test_catalog_created(self) -> None:
        catalog = Catalog.objects.get(id=1)
        self.assertEqual(catalog.nazev, "test catalog")
        self.assertEqual(catalog.products_ids, [1, 2, 3])

    def test_catalog_str(self) -> None:
        catalog = Catalog.objects.get(id=1)
        self.assertEqual(f"{catalog}", "test catalog")


class ImportCreateViewTestCase(TestCase):
    def setUp(self) -> None:
        self.attribute_value = AttributeValue.objects.create(id=1, hodnota="test value")
        self.catalog = Catalog.objects.create(
            id=1, nazev="test catalog", products_ids=[1, 2, 3]
        )
        self.client = APIClient()

    def test_post_request(self):
        data = [
            {"AttributeValue": {"id": 1, "hodnota": "test_value"}},
            {"Catalog": {"id": 1, "nazev": "test catalog"}},
        ]
        response = self.client.post("/import/", data=data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"received data": data})
        self.assertEqual(AttributeValue.objects.get(id=1).hodnota, "test value")
        self.assertEqual(Catalog.objects.get(id=1).nazev, "test catalog")
