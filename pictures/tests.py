from django.test import TestCase
from .models import Image,Category,Location 
# Create your tests here.

class CategoryTestClass(TestCase):
    '''
    test class to test methods of category class
    '''
    def setUp(self):
        self.category= Category(category="nature")

class LocationTestClass(TestCase):
    '''
    test class to test methods of the location class
    '''
    def setUp(self):
        self.location= Location(location="Nairobi")


class ImageTestClass(TestCase):
    '''
    test class to test methods of the image class
    '''
    # Set up method
    def setUp(self):
        self.category= Category(category="nature")
        self.location=  Location(location="Nairobi")
        self.image = Image(name='img1',picture='http://img1',description='nice picture',category=self.category,location=self.location)
