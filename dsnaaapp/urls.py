from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.urls.conf import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import taskCreate, taskDelete, taskDetail, taskList, taskUpdate, docCreate
urlpatterns = [
path('', views.index,name='home'),
path('dashboard',views.AdminDash,name='dashboard'),
path('dashboard/signin',views.signin,name='signin'),
path('dashboard/signup',views.register,name='singup'),
path('dashboard/users',views.users,name='users'),
path('dashboard/blog',views.blogDashboard,name='blogDashboard'),
path('dashboard/blogCreate',views.blogCreate,name='blogCreate'),
path('dashboard/blogUpdate/<int:pk>/',views.blogUpdate,name='blogUpdate'),
path('dashboard/blogDelete/<int:pk>/',views.blogDelete,name='blogDelete'),
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
path("dashboard/events", views.eventsDashboard, name="dashboardevents"),
path("dashboard/update/<int:eId>", views.UpdateEvent, name="dashboardeventsupdate"),
path("dashboard/delete/<int:pk>", views.DeleteEvent, name="dashboardeventsdelete"),
path("dashboard/mediacatergory", views.Mediadcatdashboard, name="dashboardmediacat"),
path("dashboard/mediacatergory/update/<int:Id>", views.UpdateMediadcategory, name="UpdateMediadcategory"),
path("dashboard/mediacatergory/delete/<int:pk>", views.DeleteMediaCategory, name="DeleteMc"),
path("dashboard/albums", views.Albumdashboard, name="dashboardalbum"),
path("dashboard/album/update/<int:Id>", views.UpdateAlbum, name="UpdateAlbum"),
path("dashboard/album/delete/<int:pk>", views.DeleteAlbum, name="DeleteAlbum"),
path("dashboard/images", views.Imagedashboard, name="dashboardimage"),
path("dashboard/image/update/<int:Id>", views.UpdateAlbum, name="UpdateImage"),
path("dashboard/image/delete/<int:pk>", views.DeleteAlbum, name="DeleteImage"),



path('', views.index,name='home'),
path('contact', views.contact,name='contact'),
path('blog', views.blog,name='blog'),
path('blog/search', views.search, name="blogSearch"),
path('signup',views.signup,name='signup'),
path("login", views.login_request, name="login"),
path("logout", views.logout_request, name="logout"),
path("events", views.events, name="events"),
path("library", views.library, name="library"),
path("blogDetail/<int:pk>/", views.blogDetail, name="blogDetail"),
path('tinymce/', include('tinymce.urls')),
path("searchlib", views.searchlib, name="searchlib"),
path("document/<int:id>/", views.docum, name="docum"),
path("documents/<int:id>/", views.docums, name="docums"),
path("document", views.alldocum, name="Alldocum"),
path('event/<int:id>/',views.Eventdetails,name="eventdetails"),
path('media', views.media, name="media"),
path('media/<int:id>/',views.mediapercategory,name="mediadetails"),
path('album/<int:id>/',views.imagesperalbum,name="albumdetails"),
path('aimap',views.aimap,name="aimap"),
re_path(r'^uploads/(?P<file_path>.*)/$', views.file_response_download, name='file_download'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)







