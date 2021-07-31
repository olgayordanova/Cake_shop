from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()
@admin.register(UserModel)
class CakeUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
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
