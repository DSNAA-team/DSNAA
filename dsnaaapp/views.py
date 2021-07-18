from django.urls.base import reverse
from dsnaaapp.models import ContactForm
from django.contrib.auth import authenticate, login, logout
from dsnaaapp.forms import ContactF, NewUserForm
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from typing import List
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Blog, Event, Task
from .forms import EventForm, adminForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):

    return render(request, "index.html")


def media(request):

    return render(request, "media.html")


def library(request):

    return render(request, "index.html")


def contact(request):

    if request.method == "POST":
        form = ContactF(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactF()
    return render(request, 'contact.html', {'form': form})


def blog(request):

    return render(request, "blog.html")

def events(request):
    events = Event.objects.all()
   
    return render(request, "events.html", {'events': events} )


'''event crud start'''
def eventsDashboard(request):
    events = Event.objects.all()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = EventForm()
    return render(request, "Admin/examples/dashboardevents.html", {'form': form, 'events': events})


def UpdateEvent(request, eId):
    event = get_object_or_404(Event, pk=eId)
    if request.method == 'GET':
        form = EventForm(instance=event)
        return render(request, 'Admin/examples/eventupdate.html', {'form': form, 'e_id': eId})

    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboardevents'))
        else:
            return render(request, 'Admin/examples/events.html',
                          {'form': form,
                           'msg_erreur': "Erreur d'ajout"}
                          )

def DeleteEvent(request,pk=None):
    Events = Event.objects.get(id=pk)
    Events.delete()
    return HttpResponseRedirect(reverse('dashboardevents'))

def Eventdetails(request,id):
    #projet=Projet.objects.get(pk=id)
    event=get_object_or_404(Event,pk=id)#select where id
    context={'e':event}
    return render(request,'eventdetails.html',context)    

'''event crud end'''


def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = NewUserForm()
    return render(request, 'auth/signup.html', {'f': form})


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
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="auth/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    return redirect('home')


# Create your views here.
def index(request):
    return render(request, "index.html")


def AdminDash(request):
    return render(request, "Admin/dashboard.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        mdp = request.POST['mdp']
        admin = authenticate(request, username=username, password=mdp)
        if admin is not None:

            login(request, admin)
            return redirect('/dashboard')
        else:
            messages.info(request, 'Username or login incorrecte')
            return redirect('signin')
    else:
        return render(request, "Admin/examples/signin.html")


def register(response):
    if response.method == "POST":
        form = adminForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/dashboard/signin")
    else:
        form = adminForm()
    return render(response, "Admin/examples/register.html", {"form": form})


def users(request):
    return render(request, "Admin/examples/users.html")


def blogDashboard(request):
    blogs = Blog.objects.all()
    return render(request, "Admin/examples/blogs.html", {'blogs': blogs})


class taskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)
        context['search_input'] = search_input
        return context


class taskDetail(DetailView):
    model = Task
    context_object_name = 'task'


class taskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(taskCreate, self).form_valid(form)


class taskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class taskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
