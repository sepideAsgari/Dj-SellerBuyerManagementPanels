from django.contrib import admin
from .models import User, Vendor


class BookUser(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'user_type', 'last_login')


admin.site.register(User, BookUser)


class BookVendor(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', "user_type", 'last_login')


admin.site.register(Vendor, BookVendor)
