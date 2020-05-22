from django.db import models

# Create your models here.
class Category(models.Model):
    '''
    category class to define category objects
    '''
    category = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category

class Location(models.Model):
    '''
    location class to define location objects
    '''
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location
        
class Image(models.Model):
    '''
    image class to define image objects
    '''
    name= models.CharField(max_length = 30)
    picture= models.ImageField(upload_to = 'images/')
    description= models.CharField(max_length = 100)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    location= models.ForeignKey(Location,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name

    def save_image(self):
        '''
        method that saves image to database
        '''
        self.save()    




