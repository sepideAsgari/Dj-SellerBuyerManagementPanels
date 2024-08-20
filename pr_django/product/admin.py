from django.contrib import admin
from django.db.models import Avg, Sum

from .models import Category, Product, Review

admin.site.register(Category)


class BookProduct(admin.ModelAdmin):
    list_display = ('serial', 'name', 'price', 'date_added')
admin.site.register(Product, BookProduct)


class ReviewAdmin(admin.ModelAdmin):
    # list_display = ('product', 'rating', 'total_rating1', 'avg_rate','avg_rate1')
    list_display = ('product', 'rating','total_rating1' ,'avg_rate1','createdAt')
    readonly_fields = ('createdAt','avg_rate1')

    def total_rating1(self, obj):
        return obj.product.review_set.aggregate(total=Sum('rating'))['total']
    total_rating1.short_description = 'Total Rating'

    def avg_rate1(self, obj):
        return str(round(obj.product.review_set.aggregate(average=Avg('rating'))['average'],1))
    avg_rate1.short_description = 'average Rating'


admin.site.register(Review, ReviewAdmin)

# class BookProductRate(admin.ModelAdmin):
#     list_display = ('product', 'rate', 'avg_rate', 'total_rate', 'created_at')


# admin.site.register(ProductRate, BookProductRate)
