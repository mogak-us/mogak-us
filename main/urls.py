from django.urls import path

from .views import index, record_attendance

urlpatterns = [
    path("", index),
    path("meetup/<int:meetup_id>/user/<int:user_id>/attend/", record_attendance, name="record_attendance"),
]
