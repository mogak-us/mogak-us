from django.test import TestCase
from main.models import MogakUser

class MogakUserModelTest(TestCase):

    def test_create_user(self):
        user = MogakUser.objects.create_user(
            email="testuser@example.com",
            password="testpassword123"
        )
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("testpassword123"))
