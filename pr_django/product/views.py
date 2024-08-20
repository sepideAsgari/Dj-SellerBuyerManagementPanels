from django.shortcuts import render
from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.decorators import api_view  # type: ignore

from django.db.models import Avg, Sum

from .models import Product, Category, Review
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer


class LatestProductList(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()[0:4]
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

class TopRatedProductsView(APIView):
    def get(self, request, format=None):
        top_rated_products = Product.top_rated_products()
        serializer = ProductSerializer(top_rated_products, many=True)
        return Response(serializer.data)
    
# class PopularProductList(APIView):
#     def get(self, request, format=None):
#         product = Product.objects.all()[0:4]
#         serializer = ProductSerializer(product, many=True)
#         return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

# class ReviewDetail(APIView):
#     def get_object(self, id):
#         try:
#             return Review.objects.get(id=id)
#         except Review.DoesNotExist:
#             raise Http404

#     def get(self, request, id, format=None):
#         review = self.get_object(id)
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)


class ReviewDetail(APIView):
    def get(self, request, format=None):
        # review = Review.objects.all()[0:4]
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)


class ProductAverageRatingsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = []
        for product in products:
            avg_rating = Review.objects.filter(product=product).aggregate(
                avg_rating=Avg('rating'))['avg_rating']
            data.append({
                'id': product.id,
                'name': product.name,
                'avg_rating': avg_rating
            })
        return Response(data)

    # def get_object(self, category_slug, product_slug, id):
    #     try:
    #         return Review.objects.filter(category__slug=category_slug,product__slug=product_slug).get(slug=id)
    #     except Review.DoesNotExist:
    #         raise Http404

    # def get(self, request, category_slug, product_slug, id ,format=None):
    #     review = self.get_object(category_slug, product_slug, id)
    #     serializer = ReviewSerializer(review)
    #     return Response(serializer.data)


# class ProductAverageRatingsAPIView(APIView):
#     def get_object(self, review_slug, product_rate):
#         try:
#             return Review.objects.filter(review__slug=review_slug).get(avg_rate=product_rate)
#         except Product.DoesNotExist:
#             raise Http404

#     def get(self, request, review_slug, product_rate, format=None):
#         review = self.get_object(review_slug, product_rate)
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
