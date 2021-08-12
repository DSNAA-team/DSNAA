from django.contrib import admin
from .models import Blog, Category, Documents, MediaCategory, Image, Album, Library, Task, Video, VideoLibrary
# Register your models here.

class Admin(admin.ModelAdmin) : 

    admin.site.register(Blog)
    admin.site.register(Category)
    admin.site.register(Library)
    admin.site.register(Documents)
    admin.site.register(VideoLibrary)
    admin.site.register(Video)
    admin.site.register(Album)
    admin.site.register(MediaCategory)
    admin.site.register(Image)
    admin.site.register(Task)
   

