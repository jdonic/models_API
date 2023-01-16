from django.test import TestCase
from rest_framework.test import APIClient
from .models import AttributeValue, Catalog
from django.urls import reverse


class AttributeValueTestCase(TestCase):
    """
    Test case for the AttributeValue model.
    """

    def setUp(self) -> None:
        AttributeValue.objects.create(id=1, hodnota="test value")

    def test_attribute_value_created(self) -> None:
        """
        Test that an AttributeValue instance is created with the correct value.
        """
        attribute_value = AttributeValue.objects.get(id=1)
        self.assertEqual(attribute_value.hodnota, "test value")

    def test_attribute_value_str(self) -> None:
        """
        Test the string representation of an AttributeValue instance.
        """
        attribute_value = AttributeValue.objects.get(id=1)
        self.assertEqual(f"{attribute_value}", "test value")


class CatalogTestCase(TestCase):
    """
    Test case for the Catalog model.
    """

    def setUp(self) -> None:
        Catalog.objects.create(id=1, nazev="test catalog", products_ids=[1, 2, 3])

    def test_catalog_created(self) -> None:
        """
        Test that a Catalog instance is created with the correct name and products_ids.
        """
        catalog = Catalog.objects.get(id=1)
        self.assertEqual(catalog.nazev, "test catalog")
        self.assertEqual(catalog.products_ids, [1, 2, 3])

    def test_catalog_str(self) -> None:
        """
        Test the string representation of a Catalog instance.
        """
        catalog = Catalog.objects.get(id=1)
        self.assertEqual(f"{catalog}", "test catalog")


class ImportCreateViewTestCase(TestCase):
    """Test case class for testing the import endpoint for creating new objects"""

    def setUp(self) -> None:
        """Setup test data for the test case"""
        self.attribute_value = AttributeValue.objects.create(id=1, hodnota="test value")
        self.catalog = Catalog.objects.create(
            id=1, nazev="test catalog", products_ids=[1, 2, 3]
        )
        self.client = APIClient()

    def test_post_request(self) -> None:
        """Test the post request to the import endpoint"""
        data = [
            {"attributeValue": {"id": 1, "hodnota": "test_value"}},
            {"Catalog": {"id": 1, "nazev": "test catalog"}},
        ]
        response = self.client.post("/import/", data=data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"received data": data})
        self.assertEqual(AttributeValue.objects.get(id=1).hodnota, "test value")
        self.assertEqual(Catalog.objects.get(id=1).nazev, "test catalog")


class DynamicModelListViewTests(TestCase):
    """Test the DynamicModelListView"""

    def setUp(self) -> None:
        """Initialize test client and create test catalog and attribute_value objects"""
        self.client = APIClient()
        self.catalog = Catalog.objects.create(id=1, nazev="Test Catalog")
        self.attribute_value = AttributeValue.objects.create(
            id=1, hodnota="Test Attribute Value"
        )

    def test_list_catalog(self) -> None:
        """Test that a list of catalogs is returned successfully"""
        response = self.client.get(
            reverse("dynamic_model_list", kwargs={"model_name": "catalog"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["nazev"], "Test Catalog")

    def test_list_attribute_value(self) -> None:
        """Test that a list of attribute_values is returned successfully"""
        response = self.client.get(
            reverse("dynamic_model_list", kwargs={"model_name": "attribute_value"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], 1)
        self.assertEqual(response.data[0]["hodnota"], "Test Attribute Value")

    def test_list_invalid_model(self) -> None:
        """Test that a 404 is returned when an invalid model name is passed"""
        response = self.client.get(
            reverse("dynamic_model_list", kwargs={"model_name": "invalid"})
        )
        self.assertEqual(response.status_code, 404)


class DynamicModelDetailViewTests(TestCase):
    """Test the DynamicModelDetailView"""

    def setUp(self) -> None:
        """Initialize test client and create test catalog and attribute_value objects"""
        self.client = APIClient()
        self.catalog = Catalog.objects.create(id=1, nazev="Test Catalog")
        self.attribute_value = AttributeValue.objects.create(
            id=1, hodnota="Test Attribute Value"
        )

    def test_retrieve_catalog(self) -> None:
        """Test that a catalog object is returned successfully"""
        response = self.client.get(
            reverse(
                "dynamic_model_detail",
                kwargs={"model_name": "catalog", "pk": self.catalog.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["nazev"], "Test Catalog")

    def test_retrieve_attribute_value(self) -> None:
        """Test that a attribute_value object is returned successfully"""
        response = self.client.get(
            reverse(
                "dynamic_model_detail",
                kwargs={"model_name": "attribute_value", "pk": self.attribute_value.id},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["hodnota"], "Test Attribute Value")

    def test_retrieve_invalid_model(self) -> None:
        """Test that a 404 is returned when an invalid model name is passed"""
        response = self.client.get(
            reverse("dynamic_model_detail", kwargs={"model_name": "invalid", "pk": 1})
        )
        self.assertEqual(response.status_code, 404)
