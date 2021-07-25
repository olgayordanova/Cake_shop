from django.contrib import admin

# Register your models here.

from cake_shop_app.models import Product, OrderProduct, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description', 'price')
    list_filter = ('type', )

class OrderProductAdmin ( admin.ModelAdmin ):
    list_display = ('user', 'product', 'quantity', 'ordered')
    list_filter = ('user',)

class OrderAdmin ( admin.ModelAdmin ):
    list_display = ('user', 'ordered')
    list_filter = ('user',)

    # def likes_count(self, obj):
    #     return obj.like_set.count()


admin.site.register(Product, ProductAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
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