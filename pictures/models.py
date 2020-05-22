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
    category=  category_name=models.CharField(max_length=30)
    


