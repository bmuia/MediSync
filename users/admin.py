from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Hospital

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')  
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'role', 'hospital')}),  # Added first_name and last_name
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'role', 'hospital', 'is_staff', 'is_superuser')}
        ),
    )
    filter_horizontal = ('groups', 'user_permissions')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Hospital)
