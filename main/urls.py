from django.urls import path

from .views import index, login_view, record_attendance, workspaces

urlpatterns = [
    path("", index),
    path("accounts/login/", login_view, name="login"),
    path("workspaces/", workspaces, name="workspaces"),
    path("meetup/<int:meetup_id>/attend/", record_attendance, name="record_attendance"),
]
