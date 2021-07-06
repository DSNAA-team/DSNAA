from django.contrib import admin
from .models import Blog, Category, Documents, Gallery, Image, Library, Task, Video, VideoLibrary
# Register your models here.

class Admin(admin.ModelAdmin) : 

    admin.site.register(Blog)
    admin.site.register(Category)
    admin.site.register(Library)
    admin.site.register(Documents)
    admin.site.register(VideoLibrary)
    admin.site.register(Video)
    admin.site.register(Gallery)
    admin.site.register(Image)
    admin.site.register(Task)
   

