from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.

def allPictures():
    '''
    view function to display all pictures in the application
    '''
    pictures= Image.display_images()
    return render(request, 'index.html', {"pictures" : pictures})