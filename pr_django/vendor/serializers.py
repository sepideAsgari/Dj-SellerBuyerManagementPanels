from rest_framework import serializers  # type: ignore

from .models import Product


# class RegVendorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vendor
#         fields = ('id',
#                   'full_name',
#                   'username',
#                   'email',
#                   'password'
#                   )
# class VendorInfo(serializers.ModelSerializer):
#     class Meta:
#         model = Vendor
#         fields = (
#             "id",
#             "email",
#             "username",
#         )
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vendor
#         fields = (
#             "id",
#             "full_name",
#             "email",
#             "username",
#             "password"
#         )


# class VendorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vendor
#         fields = (
#             "id",
#             "full_name",
#             "first_name",
#             "last_name",
#             "address",
#             "phone",
#             "email",
#             "mini_description",
#             "profile_picture",
#             "sales_count",
#             "is_active"
#         )


class ProductSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "description",
        )
