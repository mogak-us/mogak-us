from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from main.models import Meetup

class MeetupAuthenticationTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            email="owner@example.com",
            password="ownerpassword123"
        )
        self.meetup = Meetup.objects.create(
            owner=self.user
        )

    def test_meetup_owner_access(self):
        # Test without authentication
        response = self.client.get(f'/meetup/{self.meetup.id}/user/2/attend')
        print(response.body)
        self.assertEqual(response.status_code, 401)

        # Test with authentication
        self.client.login(email="owner@example.com", password="ownerpassword123")
        response = self.client.get(f'/meetups/{self.meetup.id}/')
        self.assertEqual(response.status_code, 200)
