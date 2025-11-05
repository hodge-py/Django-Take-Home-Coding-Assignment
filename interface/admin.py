from django.contrib import admin

from .models import ProductData, Tags  # Import the ProductData model

admin.site.register(ProductData)
admin.site.register(Tags)

# Register your models here.
