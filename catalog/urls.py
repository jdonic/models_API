from django.urls import path
from .views import AttributeValueCreateView

urlpatterns = [
    path("import/", AttributeValueCreateView.as_view(), name="import"),
]
