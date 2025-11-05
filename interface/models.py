from django.db import models

class ProductData(models.Model): # Model for product data
    product_name = models.CharField(max_length=255) # Product name field
    category = models.CharField(max_length=255) # Category field
    description = models.TextField() # Description field


class Tags(models.Model): # Model for tags
    name = models.CharField(max_length=100) # Tag name field
    product = models.ForeignKey(ProductData, on_delete=models.CASCADE) # Foreign key to ProductData


