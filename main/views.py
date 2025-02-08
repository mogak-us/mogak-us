from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from .models import Meetup, MogakUser, Attendance
from inertia import render


def index(request):
    return render(
        request,
        "Dashboard/Index",
        props={"greetings": "Django + Inertia + Vue! with Vite, it works"},
    )

@login_required
def workspaces(request):
    user = request.user
    workspaces = user.owned_workspaces()
    workspaces_json = [workspace.to_json() for workspace in workspaces]
    return render(request, "Dashboard/Workspaces", props={"workspaces": workspaces_json})

@login_required
def record_attendance(request, meetup_id, user_id):
    meetup = get_object_or_404(Meetup, id=meetup_id)
    print(meetup)
    user = get_object_or_404(MogakUser, id=user_id)
    print(user)
    attendance, created = Attendance.objects.get_or_create(meetup=meetup, user=user)
    return JsonResponse({'attended': created})
