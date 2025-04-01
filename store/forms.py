from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms



class ChangePasswordForm(SetPasswordForm):
	new_password1 = forms.CharField(label="", max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
	new_password2 = forms.CharField(label="", max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))

	class Meta:
		model = User
		fields = ['new_password1' , 'new_password2']


class UpdateUserForm(UserChangeForm):
	password = None
	username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
	 


class SignUpForm(UserCreationForm):
	username = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	password1 = forms.CharField(label="", max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
	password2 = forms.CharField(label="", max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')