from django.db import models

class ProductData(models.Model): # Model for product data
    product_name = models.CharField(max_length=255) # Product name field
    category = models.CharField(max_length=255) # Category field
    tags = models.CharField(max_length=255) # Tags field
    description = models.TextField() # Description field
