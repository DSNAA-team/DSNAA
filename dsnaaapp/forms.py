from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.db.models.enums import Choices

Roles = (
    ("1", "Admin"),
    ("2","Rédacteur")
)

class adminForm(UserCreationForm) : 
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    poste = forms.CharField(max_length=100)
    is_superuser = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    role = forms.ChoiceField(choices=Roles)

    class Meta : 
        model = User    
        fields = ('first_name','last_name','email','username','poste','is_superuser','is_staff','password1','password2','role')