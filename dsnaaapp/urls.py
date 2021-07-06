from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [

path('', views.index,name='home'),
path('contact', views.contact,name='contact'),
path('blog', views.blog,name='blog'),
path('signup',views.signup,name='signup'),
path("login", views.login_request, name="login"),
path("logout", views.logout_request, name="logout"),
path("events", views.events, name="events")


]