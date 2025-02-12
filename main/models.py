from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

ROLE = {
    'OWNER': 'Owner',
    'ADMIN': 'Admin',
    'MEMBER': 'Member'
}

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class MogakUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    meetups = models.ManyToManyField('Meetup', through='Attendance')
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def owned_workspaces(self):
        workspace_memberships = WorkspaceMembership.objects.filter(user=self, role='OWNER')
        return [membership.workspace for membership in workspace_memberships]


class Meetup(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(MogakUser, on_delete=models.CASCADE, related_name='owned_meetups', null=True)
    workspace = models.ForeignKey('Workspace', on_delete=models.CASCADE, related_name='meetups', null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    user = models.ForeignKey(MogakUser, on_delete=models.CASCADE)
    meetup = models.ForeignKey(Meetup, on_delete=models.CASCADE)
    attended_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.meetup.name}"


class Workspace(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def add_members(self, member_names: list[str]):
        for member_name in member_names:
            # Find matching alias name 
            membership = WorkspaceMembership.objects.filter(workspace=self, alias_name=member_name).first()
            if membership:
                continue
            WorkspaceMembership.objects.create(workspace=self, alias_name=member_name)


class WorkspaceMembership(models.Model):
    user = models.ForeignKey(MogakUser, on_delete=models.CASCADE, null=True)
    alias_name = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=10, choices=[(r, r) for r in ROLE.keys()], default=ROLE['MEMBER'])
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='memberships')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.workspace.name} - {self.alias_name}"


