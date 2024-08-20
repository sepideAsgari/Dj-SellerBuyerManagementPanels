from django.urls import path, include
from product import views

from .views import ProductAverageRatingsAPIView

urlpatterns = [
    path('latest-products/', views.LatestProductList.as_view()),
    path('toprated-products/', views.TopRatedProductsView.as_view()),
    path('products/search/',views.search),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('review/', views.ReviewDetail.as_view()),


    
]
