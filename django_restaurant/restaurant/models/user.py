from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.UUIDField(primary_key=True)
    mobile_number = models.CharField(max_length=12, unique=True)

    REQUIRED_FIELDS = ['id', 'first_name', 'last_name', 'mobile_number']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
