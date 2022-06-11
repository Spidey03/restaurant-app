from django.db import models


class Order(models.Model):
    id = models.UUIDField(primary_key=True)
    items = models.ManyToManyField('item')
    is_paid = models.BooleanField(default=False)
    amount = models.FloatField()

    def __str__(self):
        return {self.id}


class Cart(models.Model):
    id = models.UUIDField(primary_key=True)
    items = models.ManyToManyField('item')

    def __str__(self):
        return {self.id}