from django.contrib import admin
from .models import Vendor, Product


# class BookVendor(admin.ModelAdmin):
#     list_display = ('id', 'email', 'last_login')


# admin.site.register(Vendor, BookVendor)

admin.site.register(Product)
