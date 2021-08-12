from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import taskCreate, taskDelete, taskDetail, taskList, taskUpdate, docCreate
urlpatterns = [
path('', views.index,name='home'),
path('dashboard/signin',views.signin,name='signin'),
path('dashboard/signup',views.register,name='singup'),
path('dashboard',views.AdminDash,name='dashboard'),
path('dashboard/users',views.users,name='users'),
path('dashboard/blog',views.blogDashboard,name='blogDashboard'),
path('dashboard/createDoc',views.docCreate,name='createDoc'),
path('dashboard/updateD/<int:pId>/',views.UpdateD,name='Up'),
path('dashboard/deleteD/<int:id>/',views.DeleteD,name='DD'),
path('dashboard/createLib',views.libCreate,name='createLib'),
path('dashboard/updateL/<int:pId>/',views.UpdateL,name='Upl'),
path('dashboard/deleteL/<int:id>/',views.DeleteL,name='DL'),
path('dashboard/taskList',taskList.as_view(),name='tasks'),
path('dashboard/taskDetail/<int:pk>/',taskDetail.as_view(),name='task'),
path('dashboard/createTask',taskCreate.as_view(),name='createTask'),
path('dashboard/updateTask/<int:pk>/',taskUpdate.as_view(),name='updateTask'),
path('dashboard/deleteTask/<int:pk>/',taskDelete.as_view(),name='deleteTask'),

path('', views.index,name='home'),
path('contact', views.contact,name='contact'),
path('blog', views.blog,name='blog'),
path('signup',views.signup,name='signup'),
path("login", views.login_request, name="login"),
path("logout", views.logout_request, name="logout"),
path("events", views.events, name="events"),
path("library", views.library, name="library"),
path("searchlib", views.searchlib, name="searchlib"),
path("document/<int:id>/", views.docum, name="docum"),
path("documents/<int:id>/", views.docums, name="docums"),
path("document", views.alldocum, name="Alldocum"),
re_path(r'^uploads/(?P<file_path>.*)/$', views.file_response_download, name='file_download'),



]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
