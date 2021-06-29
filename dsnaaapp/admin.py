from django.contrib import admin
from .models import Blog, Category, Contact, Documents, Gallery, Image, Library, Video, VideoLibrary
# Register your models here.

class Admin(admin.ModelAdmin) : 

    admin.site.register(Blog)
    admin.site.register(Category)
    admin.site.register(Library)
    admin.site.register(Documents)
    admin.site.register(VideoLibrary)
    admin.site.register(Video)
    admin.site.register(Contact)
    admin.site.register(Gallery)
    admin.site.register(Image)
   

