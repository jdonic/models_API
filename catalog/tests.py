from django.test import TestCase
from rest_framework.test import APIClient
from .models import AttributeValue, Catalog
from .serializers import AttributeValueSerializer, CatalogSerializer


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


class AttributeValueListViewTestCase(TestCase):
    """Test case class for testing the attribute value list view"""

    def setUp(self) -> None:
        """Setup test data for the test case"""
        self.attribute_value1 = AttributeValue.objects.create(
            id=1, hodnota="test value 1"
        )
        self.attribute_value2 = AttributeValue.objects.create(
            id=2, hodnota="test value 2"
        )
        self.client = APIClient()

    def test_get_request(self) -> None:
        """Test the get request to the attribute value list view"""
        response = self.client.get("/detail/attribute_value/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            AttributeValueSerializer(
                [self.attribute_value1, self.attribute_value2], many=True
            ).data,
        )


class AttributeValueDetailViewTestCase(TestCase):
    """Test case class for testing the attribute value detail view"""

    def setUp(self) -> None:
        """Setup test data for the test case"""
        self.attribute_value = AttributeValue.objects.create(id=1, hodnota="test value")
        self.client = APIClient()

    def test_get_request(self) -> None:
        """Test the get request to the attribute value detail view"""
        response = self.client.get("/detail/attribute_value/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data, AttributeValueSerializer(self.attribute_value).data
        )


class CatalogListViewTestCase(TestCase):
    """Test case class for testing the catalog list view"""

    def setUp(self) -> None:
        """Setup test data for the test case"""
        self.catalog1 = Catalog.objects.create(
            id=1, nazev="test catalog 1", products_ids="[1, 2, 3]"
        )
        self.catalog2 = Catalog.objects.create(
            id=2, nazev="test catalog 2", products_ids="[4, 5, 6]"
        )
        self.client = APIClient()

    def test_get_request(self) -> None:
        """Test the get request to the catalog list view"""
        response = self.client.get("/detail/catalog/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            CatalogSerializer([self.catalog1, self.catalog2], many=True).data,
        )


class CatalogDetailViewTestCase(TestCase):
    """Test case class for testing the catalog detail view"""

    def setUp(self) -> None:
        """Setup test data for the test case"""
        self.catalog = Catalog.objects.create(
            id=1, nazev="test catalog", products_ids="[1, 2, 3]"
        )
        self.client = APIClient()

    def test_get_request(self) -> None:
        """Test the get request to the catalog detail view"""
        response = self.client.get("/detail/catalog/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, CatalogSerializer(self.catalog).data)
