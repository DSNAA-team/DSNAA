from dsnaaproject.settings import MAILCHIMP_API_KEY
from django.contrib.auth.models import User
from django.db.models import query
from dsnaaapp.models import ContactForm
from django.contrib.auth import authenticate, login, logout
from dsnaaapp.forms import ContactF, NewUserForm , blogForm
from django.shortcuts import render, redirect ,get_object_or_404
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from typing import List
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Blog, Category,Task
from .forms import adminForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count , Q
from django.conf import settings


MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

 



# Create your views here.
def index(request):
    
   
    return render(request, "index.html" )

def library(request):
    
   
    return render(request, "index.html" )    

def contact(request):
	
	if request.method == "POST":
		form = ContactF(request.POST)
		if form.is_valid():
		 form.save()
	else:
		form = ContactF()
	return render(request, 'contact.html', {'form': form})

def is_valid_search_param(param) : 
    return param != '' and param is not None


def search(request) : 
    categories = Category.objects.all()
    filteredBlogs = Blog.objects.all()
    recentPosts = Blog.objects.all().order_by('-date_creation')
    title_contains = request.GET.get('title_contains')
    title_or_author = request.GET.get('title_or_author')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')

    if is_valid_search_param(title_contains != '') :  
        filteredBlogs = filteredBlogs.filter(titre__icontains = title_contains)

    elif is_valid_search_param(title_or_author !=  '') : 
        filteredBlogs = filteredBlogs.filter(Q(titre__icontains=title_or_author) | Q(autheur__username__icontains=title_or_author)).distinct()


    if is_valid_search_param(date_min) : 
        filteredBlogs = filteredBlogs.filter(date_creation__gte=date_min)
    
    if is_valid_search_param(date_max) : 
        filteredBlogs = filteredBlogs.filter(date_creation__lt=date_max)

    if is_valid_search_param(category) : 
        filteredBlogs = filteredBlogs.filter(category__theme__icontains=category)

    params = {'filteredBlogs' : filteredBlogs , 'categories' : categories , 'recentPosts' : recentPosts}
    return render(request,"blogSearched.html",params)


def blog(request):    
    blogs = Blog.objects.all()
    categories = Category.objects.all().annotate(posts_count=Count('blog'))
    recentPosts = Blog.objects.all().order_by('-date_creation')
    return render(request, "blog.html",{"blogs" : blogs , "categories" : categories , "recentPosts" : recentPosts})
  
def blogDetail(request , pk = None) :
    blog=get_object_or_404(Blog,id=pk)
    blog.blog_views = blog.blog_views+1
    context={'blog':blog}
    blog.save()
    return render(request,'blogDetail.html',context)    


def events(request): 
    
   
    return render(request, "events.html" )   	

def signup(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=NewUserForm()
    return render(request,'auth/signup.html',{'f':form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('home')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="auth/login.html", context={"login_form":form})   



def logout_request(request):
	logout(request)
	return redirect('home')	 




        


# Create your views here.
def index(request):
    return render(request, "index.html")

def AdminDash(request) : 
    return render(request, "Admin/dashboard.html")


def signin(request) : 
    if request.method=='POST' : 
        username = request.POST['username']
        mdp = request.POST['mdp']
        admin = authenticate(request,username=username,password=mdp)
        if admin is not None :
              
            login(request,admin)
            return redirect('/dashboard')
        else : 
            messages.info(request,'Username or login incorrecte')
            return redirect('signin')
    else : 
        return render(request,"Admin/examples/signin.html")

def register(response) :
    if response.method == "POST" : 
        form = adminForm(response.POST)
        if form.is_valid() : 
            form.save()
            return redirect("/dashboard/signin")
    else : 
        form = adminForm()
    return render(response,"Admin/examples/register.html",{"form": form})


def users(request) : 
    users = User.objects.all().filter(is_superuser=False)
    return render(request, "Admin/examples/users.html",{"users":users})




def blogDashboard(request) : 
    blogs = Blog.objects.all()
    return render(request, "Admin/examples/blogsDisplay.html",{"blogs":blogs})

 
 
def blogCreate(request):
	if request.method == "POST":
		form = blogForm(request.POST,request.FILES)
		if form.is_valid():
		 form.save() 
	else:
		form = blogForm()
	return render(request, "Admin/examples/blogs.html", {"form": form})
  

def blogDelete(request , pk = None) : 
    blogs = Blog.objects.get(id=pk)
    blogs.delete()
    return HttpResponseRedirect(reverse('blogDashboard'))


def blogUpdate(request, pk =  None):
    blog = get_object_or_404(Blog, id=pk)
    if request.method == 'GET':
        form = blogForm(instance=blog)
        return render(request, 'Admin/examples/blogUpdate.html', {'form': form , 'id' : id})


    if request.method == 'POST':
        form = blogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogDashboard'))

        else:
            return render(request, 'Admin/examples/blogsDisplay.html',
                          {'form': form,
                           'msg_erreur': "Erreur d'update"}
                          )


class taskList(LoginRequiredMixin,ListView) :
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self , **kwargs) : 
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input : 
            context['tasks'] = context['tasks'].filter(
                title__icontains = search_input)
        context['search_input'] = search_input
        return context

class taskDetail(DetailView) : 
    model = Task
    context_object_name = 'task'



class taskCreate(LoginRequiredMixin,CreateView) : 
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super(taskCreate,self).form_valid(form)


class taskUpdate(LoginRequiredMixin,UpdateView) : 
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

class taskDelete(LoginRequiredMixin,DeleteView) : 
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
