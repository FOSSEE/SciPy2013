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
    links = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Link to the code (if any) or relevant links'})
    )
    attachments = forms.FileField(required=False)
    class Meta:
        model = Paper
        exclude = ('user', 'verified')
        widgets = {
        'title':forms.TextInput(attrs={'placeholder':'Title of your Talk'}),
        'objective':forms.TextInput(attrs={'placeholder':'Objective of the talk'}),
        'abstract':forms.Textarea(attrs={'placeholder':'Abstract in 400 to 700 words'}),
        'bio':forms.Textarea(attrs={'placeholder':'Tell us something about yourself in a few words'}),
    }

    def clean_attachments(self):
        cleaned_data = self.cleaned_data
        attachments = cleaned_data.get('attachments')
        if attachments:
            content_type = attachments.content_type.split('/')[1]
            content_size = attachments.size
            if not content_type in ['doc', 'docx', 'txt', 'pdf']:
                raise forms.ValidationError('Only PDF, DOC, DOCX & TXT files are allowed')
            elif content_size > 5242880:
                raise forms.ValidationError('File size exceeds 5MB')
        return attachments
