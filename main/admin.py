from django.contrib import admin
from .models import MogakUser, Meetup, Attendance

@admin.register(MogakUser)
class MogakUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    exclude = ('password', 'groups', 'user_permissions')
    readonly_fields = ('email',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('name',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'meetup', 'attended_at')
    search_fields = ('user__email', 'meetup__name')
