from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from main.models import Workspace
from ninja import NinjaAPI, Schema
from ninja.security import django_auth

api = NinjaAPI(auth=django_auth, csrf=True)

class AddMemberRequestPayload(Schema):
    member_names: list[str]


@api.post("/workspaces/{workspace_id}/members/", response={200: str})
def add_members(request, workspace_id: int, payload: AddMemberRequestPayload):
    print(request.user)
    workspace = Workspace.objects.get(id=workspace_id)
    workspace.add_members(payload.member_names)
    return "Members added successfully"
