from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class JobSystemUserCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			field = self.fields.get(field_name)  
			field.widget.attrs.update({'placeholder': field.label })

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class JobSystemUserSigninForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		for field_name in self.fields:
			field = self.fields.get(field_name)  
			field.widget.attrs.update({'placeholder': field.label })

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
