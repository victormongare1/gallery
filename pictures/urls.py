from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static


#urls
urlpatterns=[
    url(r'^$',views.allPictures,name = 'allPictures'),
    url(r'^search/',views.search_pictures,name = 'search_pictures'),
    url(r'^filterlocation/',views.filter_location,name='filter_location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)