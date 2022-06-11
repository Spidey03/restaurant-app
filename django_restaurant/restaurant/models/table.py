from django.db import models

from restaurant.models import User, Cart, Order, Restaurant


class Table(models.Model):
    id = models.UUIDField(primary_key=True)
    restaurant = models.ForeignKey(
        Restaurant,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Table {self.id}"


class TableCart(models.Model):
    id = models.UUIDField(primary_key=True)
    table_id = models.ForeignKey(
        Table, null=False, blank=False,
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        User, null=True, blank=False,
        on_delete=models.CASCADE
    )
    cart_id = models.ForeignKey(
        Cart, null=True, blank=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)


class TableOrder(models.Model):
    id = models.UUIDField(primary_key=True)
    table_id = models.ForeignKey(
        Table, null=False, blank=False,
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        User, null=True, blank=False,
        on_delete=models.CASCADE
    )
    order_id = models.ForeignKey(
        Order, null=True, blank=False,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id)
