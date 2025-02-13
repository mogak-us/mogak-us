from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.shortcuts import get_object_or_404

from main.models import Workspace, WorkspaceMembership
from ninja import NinjaAPI, Schema
from ninja.security import django_auth

api = NinjaAPI(auth=django_auth, csrf=True)

class AddMemberRequestPayload(Schema):
    member_names: list[str]

class WorkspaceMembershipResponse(Schema):
    id: int
    alias_name: str

@api.get("/workspaces/{workspace_id}/members/", response={200: list[WorkspaceMembershipResponse]})
def get_members(request, workspace_id: int):
    workspace = get_object_or_404(Workspace, id=workspace_id)
    workspace_memberships = WorkspaceMembership.objects.filter(workspace=workspace)
    members_json = [
        {
            "id": member.id,
            "alias_name": member.alias_name,
        }
        for member in workspace_memberships
    ]
    return members_json

@api.post("/workspaces/{workspace_id}/members/", response={200: str})
def add_members(request, workspace_id: int, payload: AddMemberRequestPayload):
    print(request.user)
    workspace = Workspace.objects.get(id=workspace_id)
    workspace.add_members(payload.member_names)
    return "Members added successfully"
