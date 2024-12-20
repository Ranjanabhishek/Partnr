from django.db import models

class ProductTable(models.Model):
    name  = models.CharField()
    description = models.TextField()
    price = models.DecimalField()
    stock = models.IntegerField()
    created_at = models.TimeField()
    updates_at = models.TimeField()

class Users(models.Model):
    name  = models.CharField()
    phone = models.CharField()
    email = models.CharField()
    address = models.TextField()
    created_at = models.TimeField()
    updates_at = models.TimeField()

class Shoppingcart(models.Model):
    cart_name  = models.CharField()
    cart_id = models.CharField()
    created_at = models.TimeField()
    updates_at = models.TimeField()
    product_id = models.CharField()
    product_name = models.CharField()


