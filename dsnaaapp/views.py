from django.urls.base import reverse
from dsnaaapp.models import ContactForm
from django.contrib.auth import authenticate, login, logout
from dsnaaapp.forms import ContactF, NewUserForm
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
    
   
    return render(request, "index.html" )
    

def contact(request):
	
	if request.method == "POST":
		form = ContactF(request.POST)
		if form.is_valid():
		 form.save()
	else:
		form = ContactF()
	return render(request, 'contact.html', {'form': form})

def blog(request):
    
   
    return render(request, "blog.html" )     


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




        