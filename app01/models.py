from django.db import models


class Admin(models.Model):
    """Administrator Table"""
    username = models.CharField(verbose_name="Username", max_length=16)
    password = models.CharField(verbose_name="Password", max_length=64)


class Department(models.Model):
    """Department Table"""
    depart = models.CharField(verbose_name="Department", max_length=32)


class AssetSet(models.Model):
    """Asset Table"""
    des = models.CharField(verbose_name="Description", max_length=64)
    price = models.IntegerField(verbose_name="Price")
    category = models.SmallIntegerField(verbose_name="Category", choices=((1, "Office"), (2, "3C"), (3, "Real Estate")))
    depart = models.ForeignKey(verbose_name="FK_Department", to="Department", to_field="id", on_delete=models.CASCADE)

