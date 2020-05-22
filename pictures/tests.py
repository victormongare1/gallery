from django.test import TestCase
from .models import Image,Category,Location 
# Create your tests here.

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.image = Image(name='img1',picture='http://img1',description='nice picture',category=self.category,location=self.location)
