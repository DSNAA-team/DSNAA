from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

path('', views.index,name='home'),
path('dashboard/signin',views.signin,name='signin'),
path('dashboard/signup',views.register,name='singup'),
path('dashboard',views.AdminDash,name='dashboard'),
path('dashboard/users',views.users,name='users'),
path('dashboard/blog',views.blog,name='blog'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)