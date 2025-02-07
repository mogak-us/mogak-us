from django.contrib import admin
from .models import MogakUser

@admin.register(MogakUser)
class MogakUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    exclude = ('password', 'groups', 'user_permissions')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
