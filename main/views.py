from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Meetup, MogakUser, Attendance
from inertia import render


def index(request):
    return render(
        request,
        "Dashboard/Index",
        props={"greetings": "Django + Inertia + Vue! with Vite, it works"},
    )

def delete_meetup(request, meetup_id):
    if request.method == "POST":
        meetup = get_object_or_404(Meetup, id=meetup_id)
        meetup.delete()
        return JsonResponse({'deleted': True})
    return HttpResponseNotAllowed(['POST'])
def record_attendance(request, meetup_id, user_id):
    meetup = get_object_or_404(Meetup, id=meetup_id)
    user = get_object_or_404(MogakUser, id=user_id)
    attendance, created = Attendance.objects.get_or_create(meetup=meetup, user=user)
    return JsonResponse({'attended': created})
