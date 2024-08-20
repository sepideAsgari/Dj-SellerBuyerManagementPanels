from rest_framework import serializers  # type: ignore

from .models import User, Vendor
# from order.serializers import MyOrderSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "full_name",
            "username",
            "email",
            "user_type",
            "province",
            "city",
        )


class VendorInfo(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            "id",
            "email",
            "username",
            "user_type",
            "province",
            "city",
        )
