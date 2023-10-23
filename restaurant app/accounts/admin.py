from django.contrib import admin
from . import models
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ngettext


class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    actions = ['mark_as_customer']
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined', )
    filter_horizontal = tuple()
    list_filter = tuple()
    fieldsets = tuple()
    
    @admin.action(description='Mark selected users as customer')
    def mark_as_customer(self, request, queryset):
        updated = queryset.update(role=2)
        self.message_user(request, ngettext('%d user was  successfully marked as customer.', '%d users were successfully marked as customer', updated) % updated, messages.SUCCESS)
    
    
    
admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.UserProfile)