from typing import List
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Blog, Category,Task
from .forms import adminForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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
    return render(request, "Admin/examples/users.html")


def blog(request) : 
    blogs = Blog.objects.all()
    return render(request, "Admin/examples/blogs.html",{'blogs':blogs})



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
