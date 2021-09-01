from dsnaaapp.models import ContactForm, Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django import forms
from django.db.models import fields
from django.db.models.enums import Choices




# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ContactF(ModelForm):
	class Meta:
		model = ContactForm
		fields = '__all__'



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



class blogForm(ModelForm) : 
	category = forms.Select()
	autheur = forms.Select()
	titre = forms.CharField(max_length=50)
	slug = forms.CharField()
	content =  forms.CharField()
	image =  forms.ImageField()
	class Meta : 
		model = Blog
		fields = ('category','autheur','titre','slug','content','image')
		

