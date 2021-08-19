import os
from django.http.response import FileResponse, Http404
from dsnaaapp.filters import DocFilter, LibFilter, LibraryFilter
from dsnaaapp.models import ContactForm
from django.contrib.auth import authenticate, login, logout
from dsnaaapp.forms import ContactF, NewUserForm
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
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
from .models import Blog, Documents, Library, Task
from .forms import adminForm, documents_form, library_form
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Album, Blog, Event, Image, MediaCategory, Task
from .forms import AlbumForm, EventForm, ImageForm, MediacatForm, adminForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):

    return render(request, "index.html")


def alldocum(request):
    doc = Documents.objects.all()
    myfilter = DocFilter(request.GET, queryset=doc)
    doc = myfilter.qs
    context = {'doc': doc,'myfilter':myfilter}

    return render(request, "documents.html",context)

def docum(request,id):
    docs = Documents.objects.all()
    projet = get_object_or_404(Library, pk=id)  # select where id
    myfilter = LibFilter(request.GET, queryset=docs)
    docs = myfilter.qs
    images = projet.document.all()

    context = {'p': projet,'docs':docs,'images':images,'myfilter':myfilter}
    return render(request, "documents_detail.html",context)

def docums(request,id):
    doc = Documents.objects.all()
    projet = get_object_or_404(Documents, pk=id)  # select where id
    myfilter = DocFilter(request.GET, queryset=doc)
    doc = myfilter.qs
    context = {'p': projet,'doc':doc,'myfilter':myfilter}
    return render(request, "Doc_One.html",context)

def searchlib(request):
    if request.method == "POST":
        searched = request.POST['searched']
        lib = Library.objects.filter(titre__contains=searched)
        return render(request, "searchlib.html", {'searched': searched, 'lib': lib})
    else:
        return render(request, "searchlib.html", {})


def library(request):
    doc = Documents.objects.all()
    lib = Library.objects.all()
    myfilter = LibraryFilter(request.GET, queryset=lib)
    lib = myfilter.qs

    context = {'lib': lib, 'doc': doc, 'myfilter': myfilter}
    return render(request, "library.html", context)
def media(request):
    mediacat = MediaCategory.objects.all()
  
    albums = Album.objects.all()
    return render(request, "media.html", {'mediacat': mediacat , 'albums': albums } )

def mediapercategory(request,id):
    mediacat = MediaCategory.objects.all()
    mc = get_object_or_404(MediaCategory , pk=id)
   
  
    albums = mc.album_set.all()
    return render(request, "albumpercategory.html", {'mediacat': mediacat , 'albums': albums } )

def imagesperalbum(request,id):
    '''images = Image.objects.all()'''
    album = get_object_or_404(Album , pk=id)
   
  
    images = album.image_set.all()
    return render(request, "imagesperalbum.html", {'images': images , 'album' : album  } )



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
        return render(request, 'Admin/examples/updateform.html', {'form': form, 'e_id': eId})

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

'''mediacategory crud start'''
def Mediadcatdashboard(request):
    mediacat = MediaCategory.objects.all()
    if request.method == "POST":
        form = MediacatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MediacatForm()
    return render(request, "Admin/examples/dashboardmediacategory.html", {'form': form, 'mediacat': mediacat})


def UpdateMediadcategory(request, Id):
    mediacat = get_object_or_404(MediaCategory, pk=Id)
    if request.method == 'GET':
        form = MediacatForm(instance=mediacat)
        return render(request, 'Admin/examples/updateform.html', {'form': form, 'mc_id': Id})

    if request.method == 'POST':
        form = MediacatForm(request.POST,request.FILES, instance=mediacat)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboardmediacat'))
        else:
            return render(request, 'Admin/examples/dashboardmediacategory.html',
                          {'form': form,
                           'msg_erreur': "Erreur d'ajout"}
                          )

def DeleteMediaCategory(request,pk=None):
    mc = MediaCategory.objects.get(id=pk)
    mc.delete()
    return HttpResponseRedirect(reverse('dashboardmediacat'))



'''mediacategory crud end'''



'''album crud start'''

'''add & display'''
def Albumdashboard(request):
    albums = Album.objects.all()
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AlbumForm()
    return render(request, "Admin/examples/dashboardalbum.html", {'form': form, 'albums': albums})




def UpdateAlbum(request, Id):
    album = get_object_or_404(Album, pk=Id)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
        return render(request, 'Admin/examples/updateform.html', {'form': form, 'al_id': Id})

    if request.method == 'POST':
        form = AlbumForm(request.POST,request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboardalbum'))
        else:
            return render(request, 'Admin/examples/dashboardalbum.html',
                          {'form': form,
                           'msg_erreur': "Erreur d'ajout"}
                          )

def DeleteAlbum(request,pk=None):
    mc = Album.objects.get(id=pk)
    mc.delete()
    return HttpResponseRedirect(reverse('dashboardalbum'))


'''album crud end'''

'''add & display'''
def Imagedashboard(request):
    images = Image.objects.all()
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    return render(request, "Admin/examples/dashboardimage.html", {'form': form, 'images': images})


def UpdateImage(request, Id):
    image = get_object_or_404(Image, pk=Id)
    if request.method == 'GET':
        form = ImageForm(instance=image)
        return render(request, 'Admin/examples/updateform.html', {'form': form, 'img_id': Id})

    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboardimage'))
        else:
            return render(request, 'Admin/examples/dashboardimage.html',
                          {'form': form,
                           'msg_erreur': "Erreur d'ajout"}
                          )

def DeleteAlbum(request,pk=None):
    img = Image.objects.get(id=pk)
    img.delete()
    return HttpResponseRedirect(reverse('dashboardimage'))


'''image crud start'''

'''image crud end'''

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


@csrf_exempt
def docCreate(request):
    doc = Documents.objects.all()
    if request.method == "GET":
        form = documents_form()
        return render(request, 'dsnaaapp/documents_form.html', {'form': form, 'doc': doc})
    if request.method == 'POST':
        form = documents_form(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('createDoc'))
        else:
            return render(request, 'dsnaaapp/documents_form.html', {'form': form, 'doc': doc, 'msg_erreur': "Erreur d'ajout"})


def UpdateD(request, pId):
    Document = get_object_or_404(Documents, pk=pId)  # select where id
    if request.method == "GET":
        form = documents_form(instance=Document)
        return render(request, "dsnaaapp/updateD.html", {"form": form, 'p_id': pId})
    if request.method == 'POST':
        form = documents_form(request.POST, request.FILES, instance=Document)
        if form.is_valid():
            form.save()  # flush in symphony
            return HttpResponseRedirect(reverse('createDoc'))
        else:
            return render(request, 'dsnaaapp/updateD.html', {'form': form, 'p_id': pId, 'msg_erreur': "Erreur d'update"})


def DeleteD(request, id):
    Document = get_object_or_404(Documents, pk=id)  # select where id
    Document.delete()
    return HttpResponseRedirect(reverse('createDoc'))


@csrf_exempt
def libCreate(request):
    doc = Documents.objects.all()
    lib = Library.objects.all()
    if request.method == "GET":
        form = library_form()
        return render(request, 'dsnaaapp/library_form.html', {'form': form, 'lib': lib, 'doc': doc})
    if request.method == 'POST':
        form = library_form(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponseRedirect(reverse('createLib'))
        else:
            return render(request, 'dsnaaapp/library_form.html', {'form': form, 'lib': lib, 'doc': doc, 'msg_erreur': "Erreur d'ajout"})


def UpdateL(request, pId):
    library = get_object_or_404(Library, pk=pId)  # select where id
    if request.method == "GET":
        form = library_form(instance=library)
        return render(request, "dsnaaapp/updateL.html", {"form": form, 'p_id': pId})
    if request.method == 'POST':
        form = library_form(request.POST, request.FILES, instance=library)
        if form.is_valid():
            form.save()  # flush in symphony
            return HttpResponseRedirect(reverse('createLib'))
        else:
            return render(request, 'dsnaaapp/updateL.html', {'form': form, 'p_id': pId, 'msg_erreur': "Erreur d'update"})


def DeleteL(request, id):
    library = get_object_or_404(Library, pk=id)  # select where id
    library.delete()
    return HttpResponseRedirect(reverse('createLib'))


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

# Case 5 Limit file download type - recommended
def file_response_download(request, file_path):
    ext = os.path.basename(file_path).split('.')[-1].lower()
    # cannot be used to download py, db and sqlite3 files.
    if ext not in ['py', 'db',  'sqlite3']:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        raise Http404

# Map Test
