from django.test import TestCase
from skatebooks.models import User, Spot

# Create your tests here.

class UserObjectsTestCase(TestCase):
    def test_user_objects(self):
        users = User.objects.all()
        for user in users:
            return user
        
class SpotObjectsTestCase(TestCase):
    def test_spot_objects(self):
        spots = Spot.objects.all()
        for spot in spots:
            return spot
        



