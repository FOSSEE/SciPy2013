from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from website.models import Paper

class UserLoginForm(forms.Form):
	username = forms.CharField(
			widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), 
			label=''
		)
	password = forms.CharField(
			widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), 
			label=''
		)
	
class UserRegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
	password = forms.CharField(widget=forms.PasswordInput())
	password1 = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', 'username')

class DocumentUploadForm(forms.ModelForm):

  class Meta:
    model = Paper
    exclude = ('user', 'verified')
