from django.contrib import admin

from .models import Order, OrderItem



# 00000000000000000000000000000000000000000000000000000000000000000000000

# class BookOrder(admin.ModelAdmin):
#     list_display = ('id', 'status', 'created_at')


# admin.site.register(Order, BookOrder)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('id', 'status', 'created_at')

admin.site.register(Order, OrderAdmin)


# 00000000000000000000000000000000000000000000000000000000000000000000000

class BookOrderItem(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')


admin.site.register(OrderItem, BookOrderItem)
