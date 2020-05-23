from django.test import TestCase
from .models import Image,Category,Location 
# Create your tests here.

class CategoryTestClass(TestCase):
    '''
    test class to test methods of category class
    '''
    # Set up method
    def setUp(self):
        self.category= Category(category="nature")

    #testing class instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))  

    # Testing Save Method
    def test_save_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)      

class LocationTestClass(TestCase):
    '''
    test class to test methods of the location class
    '''
    # Set up method
    def setUp(self):
        self.location= Location(location="Nairobi")

    #testing class instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    # Testing Save Method
    def test_save_method(self):
        self.location.save_location()
        locations= Location.objects.all()
        self.assertTrue(len(locations) > 0)

class ImageTestClass(TestCase):
    '''
    test class to test methods of the image class
    '''
    # Set up method
    def setUp(self):
        self.category= Category(category="nature")
        self.location=  Location(location="Nairobi")
        self.image = Image(name='img1',picture='http://img1',description='nice picture',category=self.category,location=self.location)

    #testing class instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)    