from django.db import models


class Item(models.Model):
    id = models.UUIDField(primary_key=True)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=50)
    price = models.FloatField(null=False)

    def __str__(self):
        return str(self.id)