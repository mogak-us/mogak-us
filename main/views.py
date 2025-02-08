from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render as django_render
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
def record_attendance(request, meetup_id, user_id):
    meetup = get_object_or_404(Meetup, id=meetup_id)
    print(meetup)
    user = get_object_or_404(MogakUser, id=user_id)
    print(user)
    attendance, created = Attendance.objects.get_or_create(meetup=meetup, user=user)
    return JsonResponse({'attended': created})
