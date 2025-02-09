from django.urls import path

from .api import api
from .views import add_members, index, login_view, record_attendance, meetup_list, workspace_detail, workspaces, meetup_detail

urlpatterns = [
    path("", index),
    path("api/", api.urls),
    path("accounts/login/", login_view, name="login"),
    path("workspaces/", workspaces, name="workspaces"),
    path("workspaces/<int:workspace_id>/", workspace_detail, name="workspace_detail"),
    path("workspaces/<int:workspace_id>/meetups", meetup_list, name="meetup_list"),
    path("workspaces/<int:workspace_id>/meetups/<int:meetup_id>/", meetup_detail, name="meetup_detail"),
    path("meetup/<int:meetup_id>/attend/", record_attendance, name="record_attendance"),
]
