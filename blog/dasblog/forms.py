# Import django forms module
from django import forms
# And the django.contrib.admin.forms.AdminAuthenticationForm class
from django.contrib.admin.forms import AdminAuthenticationForm

class SearchForm(forms.Form):
	"""
	Form inherited class representing the SearchForm used in the SearchFormView class.
	"""
	string = forms.CharField(label="",
							max_length=200,
							min_length=1,
							initial="JAN 2, 2012-01-11, Django, Uncategorized, Mission Accomplished...",
							widget=forms.TextInput(attrs={'size': 65,})
							)

class HiddenAdminForm(AdminAuthenticationForm):
	"""
	AdminAuthenticationForm inherited class representing the quicklogin form used in almost all
	the views and in the quicklogin.html template.
	"""
	username = forms.CharField(label="Username",
							max_length=30,
							initial="username",
							widget=forms.TextInput(attrs={'size':12,}))
	password = forms.CharField(label="Password",
							initial="password",
							widget=forms.PasswordInput(attrs={'size':12,}))