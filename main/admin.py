from django.contrib import admin
from .models import MogakUser, Meetup, Attendance, Workspace, WorkspaceMembership

@admin.register(MogakUser)
class MogakUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    exclude = ('password', 'groups', 'user_permissions')
    readonly_fields = ('email',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'owner')
    search_fields = ('name', 'owner__email')
    list_filter = ('date', 'owner')
    ordering = ('date',)

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(WorkspaceMembership)
class WorkspaceMembershipAdmin(admin.ModelAdmin):
    list_display = ('workspace', 'alias_name', 'role', 'user', 'joined_at')
    search_fields = ('workspace__name', 'alias_name', 'user__email')
    list_filter = ('role', 'workspace')
    ordering = ('workspace', 'alias_name')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'meetup', 'attended_at')
    search_fields = ('user__email', 'meetup__name')
    list_filter = ('attended_at', 'meetup')
    ordering = ('attended_at',)
