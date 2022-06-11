from django.db import models

from restaurant.models import Item


class Order(models.Model):
    id = models.UUIDField(primary_key=True)
    items = models.ManyToManyField(Item)
    is_paid = models.BooleanField(default=False)
    amount = models.FloatField()

    def __str__(self):
        return {self.id}


class Cart(models.Model):
    id = models.UUIDField(primary_key=True)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return {self.id}