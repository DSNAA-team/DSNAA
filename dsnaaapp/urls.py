from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import taskCreate, taskDelete, taskDetail, taskList, taskUpdate
urlpatterns = [
path('', views.index,name='home'),
path('dashboard/signin',views.signin,name='signin'),
path('dashboard/signup',views.register,name='singup'),
path('dashboard',views.AdminDash,name='dashboard'),
path('dashboard/users',views.users,name='users'),
path('dashboard/blog',views.blogDashboard,name='blogDashboard'),
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
path("dashboard/events", views.eventsDashboard, name="dashboardevents"),
path("dashboard/update/<int:eId>", views.UpdateEvent, name="dashboardeventsupdate"),
path("dashboard/delete/<int:pk>", views.DeleteEvent, name="dashboardeventsdelete"),
path("library", views.library, name="library"),
path('media', views.media, name="media")


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)