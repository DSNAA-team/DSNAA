from typing import Text
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.db.models.fields import NullBooleanField




'''Class category'''

class Category(models.Model) : 
    theme = models.TextField(max_length=50)
    def __str__(self) :
        return self.theme


'''Class Blog , relation FK avec class Categorie'''

class Blog(models.Model) : 
    category = models.ForeignKey(Category,on_delete=CASCADE,null=True)
    autheur = models.ForeignKey(User,on_delete=CASCADE,null=True)
    titre = models.CharField(max_length=255,null=True)
    slug = models.SlugField(null=True)
    content = models.TextField(max_length=2500,null=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)
    image = models.ImageField(null=True)
    def __str__(self) :
        return self.titre


'''Class library'''

class Library(models.Model) : 
    titre = models.TextField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.titre


'''Class Documents , relation manytomany avec class library'''

class Documents(models.Model) : 
    titre = models.TextField(max_length=255)
    autheur = models.TextField(max_length=50)
    organization = models.TextField(max_length=100)
    date_publication = models.DateField()
    library = models.ManyToManyField(Library)
    fichier = models.FileField()
    reference = models.TextField(max_length=50)
    editeur = models.TextField(max_length=50)
    lien = models.TextField(max_length=100)
    thumbnail = models.ImageField()
    def __str__(self) :
        return self.titre


'''Class Galery '''
class MediaCategory(models.Model) : 
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    thumbnail = models.ImageField(null=True)
    def __str__(self) :
        return self.title

        
class Album(models.Model) : 
    
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(null=True)
    Category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE)
    def __str__(self) :
        return self.title





'''Class Image '''

class Image(models.Model) : 
    titre = models.TextField(max_length=255)
    description = models.TextField(max_length=500)
    date_publication = models.DateTimeField(auto_now_add=True)
    lieu = models.TextField(max_length=40)
    image = models.ImageField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE,null=True)
    def __str__(self) :
        return self.titre


    
'''Class VideoLibrary '''

class VideoLibrary(models.Model) : 
    titre = models.TextField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    theme = models.TextField(max_length=25)
    def __str__(self) :
        return self.titre


'''Class Video '''

class Video(models.Model) : 
    titre = models.TextField(max_length=255)
    date_publication = models.DateTimeField(auto_now_add=True)
    organisation = models.TextField(max_length=40)
    longueur = models.FloatField()
    description = models.TextField(max_length=255)
    lien = models.TextField(max_length=100)
    videoLibrary = models.ManyToManyField(VideoLibrary)
    def __str__(self) :
        return self.titre

'''Class Task'''

class Task(models.Model) : 
    user = models.ForeignKey(User,on_delete=CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.title
    
    class Meta : 
        ordering = ['complete']


'''Class evenement'''
class Event(models.Model) : 
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    date_event = models.DateField()
    organizer = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    place = models.CharField(null=True,max_length=50)
    image = models.ImageField(null=True,upload_to = "images/")
    def __str__(self) :
        return self.title


'''Class fomrulaire contact'''
class ContactForm(models.Model):
     message=models.TextField()
     name=models.CharField(max_length=50)
     email=models.EmailField(max_length=50)
     subject=models.CharField(max_length=100)






    





    




    









