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

    @classmethod
    def display_images():
        '''
        method that shows all images in the database
        '''
        pictures=cls.objects.all()
        return pictures

    @classmethod
    def delete_image(cls,id):
        '''
        method that deletes image from database
        '''
        cls.objects.filter(id=id).delete()

    @classmethod
    def search_image(cls,search_term):
        '''
        method that retrieves images based on their category
        '''
        pictures = cls.objects.filter(category__category__icontains=search_term)
        return pictures   

    @classmethod
    def filter_by_location(cls,search_term):
        '''
        method that rerieves images based on the location they were taken
        '''
        pictures = cls.objects.filter(location__location__icontains=search_term)
        return pictures   





