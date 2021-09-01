from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import taskCreate, taskDelete, taskDetail, taskList, taskUpdate

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
path('dashboard/taskList',taskList.as_view(),name='tasks'),
path('dashboard/taskDetail/<int:pk>/',taskDetail.as_view(),name='task'),
path('dashboard/createTask',taskCreate.as_view(),name='createTask'),
path('dashboard/updateTask/<int:pk>/',taskUpdate.as_view(),name='updateTask'),
path('dashboard/deleteTask/<int:pk>/',taskDelete.as_view(),name='deleteTask'),
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
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
