from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Blog
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
        form = super(UserCreationForm(response.POST))
        if form.is_valid() : 
            form.save()
            return redirect("/dashboard/signin")
    else : 
        form = UserCreationForm()
    return render(response,"Admin/examples/register.html",{"form": form})


def users(request) : 
    return render(request, "Admin/examples/tables.html")


def blog(request) : 
    blogs = Blog.objects.all()
    return render(request, "Admin/examples/profile.html",{'blogs':blogs})