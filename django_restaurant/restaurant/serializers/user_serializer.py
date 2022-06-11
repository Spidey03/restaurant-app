from rest_framework import serializers

from restaurant.models import User


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100, allow_null=False)
    mobile_number = serializers.CharField(max_length=12, allow_null=False)

    class Meta:
        model = User
        fields = ['__all__']
