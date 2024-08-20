from rest_framework import serializers  # type: ignore

from .models import Category, Product, Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "averageReview",
            "countReview",
            "get_image",
            "get_thumbnail",
            "get_make_product_image",
            "get_category_name"
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )


class ReviewSerializer (serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id',
                  'product',
                  'user',
                  'rating',
                  'comment',
                  'createdAt',
                  'is_active',
                  'avg_rate',
                  'is_verify'
                  )


# class ProductRateSerializer (serializers.ModelSerializer):
#     class Meta:
#         model = ProductRate
#         fields = ('id',
#                   'product',
#                   'user',
#                   'rate',
#                   'avg_rate',
#                   'total_rate',
#                   'created_at'
#                   )
        
    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')
    #     order = Review.objects.create(**validated_data)

    #     for item_data in items_data:
    #         ProductRate.objects.create(order=order, **item_data)
            
    #     return order