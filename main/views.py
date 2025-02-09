from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render as django_render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from .models import Meetup, MogakUser, Attendance, Workspace
from inertia import render


def index(request):
    return render(
        request,
        "Dashboard/Index",
        props={"greetings": "Django + Inertia + Vue! with Vite, it works"},
    )

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            next_path = request.GET.get('next')
            if next_path:
                return redirect(next_path) 

            return redirect('workspaces')
        else:
            return django_render(request, 'login.html', {'error': 'Invalid credentials'})
    return django_render(request, 'accounts/login.html')

@login_required
def workspaces(request):
    user = request.user
    workspaces = user.owned_workspaces()
    workspaces_json = [
        {
            "id": workspace.id,
            "name": workspace.name,
        }
        for workspace in workspaces
    ]
    return render(request, "Dashboard/Workspaces", props={"workspaces": workspaces_json})

@login_required 
def meetup_list(request, workspace_id):
    workspace = get_object_or_404(Workspace, id=workspace_id)
    meetups = workspace.meetups.all()
    meetups_json = [
        {
            "id": meetup.id,
            "name": meetup.name,
            "date": meetup.date,
        }
        for meetup in meetups
    ]
    return render(request, "Dashboard/MeetupList", props={
        "meetups": meetups_json,
        "workspace": {
            "id": workspace.id,
            "name": workspace.name,
        }
    })

@login_required 
def meetup_detail(request, workspace_id, meetup_id):
    workspace = get_object_or_404(Workspace, id=workspace_id)
    meetup = get_object_or_404(Meetup, id=meetup_id)
    if meetup.workspace != workspace:
        return HttpResponseNotAllowed()

    return render(request, "Dashboard/MeetupDetail", props={
        "workspace": {
            "id": workspace.id,
            "name": workspace.name,
        },
        "meetup": {
            "id": meetup.id,
            "name": meetup.name,
            "date": meetup.date,
        }
    })


@login_required 
def workspace_detail(request, workspace_id):
    workspace = get_object_or_404(Workspace, id=workspace_id)
    meetups = workspace.meetups.all()
    meetups_json = [ 
        {
            "id": meetup.id,
            "name": meetup.name,
            "date": meetup.date,
        }
        for meetup in meetups
    ]
    return render(request, "Dashboard/WorkspaceDetail", props={
        "workspace": {
            "id": workspace.id,
            "name": workspace.name,
        },
        "meetups": meetups_json,
    })


@login_required
def record_attendance(request, meetup_id, user_id):
    meetup = get_object_or_404(Meetup, id=meetup_id)
    print(meetup)
    user = get_object_or_404(MogakUser, id=user_id)
    print(user)
    attendance, created = Attendance.objects.get_or_create(meetup=meetup, user=user)
    return JsonResponse({'attended': created})
