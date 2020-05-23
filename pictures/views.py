from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.

def allPictures(request):
    '''
    view function to display all pictures in the application
    '''
    pictures= Image.display_images()
    return render(request, 'index.html', {"pictures" : pictures})

def search_pictures(request):
    '''
    view function to display the searched pictures by category
    '''
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_images": searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})

def filter_location(request):
    if 'location' in request.GET and request.GET["location"]:
        search_term=request.GET.get("location")
        searched_locations=Image.filter_by_location(search_term)
        message=f"{search_term}"

        return render(request,'searchlocation.html',{"message":message,"locations":searched_locations})
    else:
        message ="You haven't searched for any location"
        return render(request,'searchlocation.html',{"message":message})