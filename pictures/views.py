from django.shortcuts import render
from django.http  import HttpResponse,Http404

# Create your views here.

def allPictures():
    '''
    view function to display all pictures in the application
    '''
    pictures=None
    return render(request, 'index.html', {"pictures":pictures})