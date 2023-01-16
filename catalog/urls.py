from django.urls import path
from .views import ImportCreateView, DynamicModelListView, DynamicModelDetailView

urlpatterns = [
    path("import/", ImportCreateView.as_view(), name="import"),
    path(
        "detail/<str:model_name>/",
        DynamicModelListView.as_view(),
        name="dynamic_model_list",
    ),
    path(
        "detail/<str:model_name>/<int:pk>/",
        DynamicModelDetailView.as_view(),
        name="dynamic_model_detail",
    ),
]
