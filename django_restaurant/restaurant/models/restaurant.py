from django.db import models


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
