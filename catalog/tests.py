from django.test import TestCase
from .models import AttributeValue, Catalog


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
