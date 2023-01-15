from django.urls import path
from .views import (
    ImportCreateView,
    AttributeValueListView,
    AttributeValueDetailView,
    CatalogListView,
    CatalogDetailView,
)

urlpatterns = [
    path("import/", ImportCreateView.as_view(), name="import"),
    path("detail/attribute_value/", AttributeValueListView.as_view(), name="attr_list"),
    path(
        "detail/attribute_value/<int:pk>/",
        AttributeValueDetailView.as_view(),
        name="attr_detail",
    ),
    path("detail/catalog/", CatalogListView.as_view(), name="catalog_list"),
    path(
        "detail/catalog/<int:pk>/", CatalogDetailView.as_view(), name="catalog_detail"
    ),
]
