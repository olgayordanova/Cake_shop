from django.contrib import admin

# Register your models here.

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







# admin.site.register(Product)





# admin.site.register(CakeShopUser)
# admin.site.register(Profile)
#
# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#
# # from blog_system.authentication.models import Profile
# from profiles.models import Profile
#
# UserModel = get_user_model()
#
#
# class ProfileInlineAdmin(admin.StackedInline):
#     model = Profile
#     verbose_name_plural = 'Profile'
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (
#         ProfileInlineAdmin,
#     )
#
#
# admin.site.unregister(UserModel)
# admin.site.register(UserModel, UserAdmin)