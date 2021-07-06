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
path('dashboard/blog',views.blog,name='blog'),
path('dashboard/taskList',taskList.as_view(),name='tasks'),
path('dashboard/taskDetail/<int:pk>/',taskDetail.as_view(),name='task'),
path('dashboard/createTask',taskCreate.as_view(),name='createTask'),
path('dashboard/updateTask/<int:pk>/',taskUpdate.as_view(),name='updateTask'),
path('dashboard/deleteTask/<int:pk>/',taskDelete.as_view(),name='deleteTask')

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)