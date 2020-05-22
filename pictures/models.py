from django.db import models

# Create your models here.

class Image(models.Model):
    '''
    image class to define image objects
    '''
    name= models.CharField(max_length = 30)
    picture= models.ImageField(upload_to = 'images/')
    description= models.CharField(max_length = 100)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    location= models.ForeignKey(Location,on_delete=models.CASCADE)
 
class Category(models.Model):
    '''
    category class to define category objects
    '''
    category = models.CharField(max_length=30)

class Location(models.Model):
    '''
    location class to define location objects
    '''
    location = models.CharField(max_length=30)
        


