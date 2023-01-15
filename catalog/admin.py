from django.contrib import admin

# Register your models here.
from .models import AttributeValue, Catalog


admin.site.register(AttributeValue)
admin.site.register(Catalog)
