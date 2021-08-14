from django.contrib import admin

from cake_shop_app.models import Product, OrderItem, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'price')
    list_filter = ('type', )

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_ordered', 'complete')
    list_filter = ('user',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'quantity')
    list_filter = ('user',)

admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)

