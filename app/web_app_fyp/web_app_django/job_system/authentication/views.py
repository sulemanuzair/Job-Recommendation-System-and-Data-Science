from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import *
from .forms import JobSystemUserCreationForm

@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
@applicant_to_root
def index(request):
	return render(request, 'authentication/index.html')

@unauthenticated_user_only
def register(request):
	# if request.user.is_authenticated:
	# 	return redirect('index')

	if request.method == 'POST':
		form = JobSystemUserCreationForm(request.POST)	
		
		if form.is_valid():
			user = form.save()
			
			group = Group.objects.get(name='applicant')
			user.groups.add(group)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password1'] #try just password as well
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = JobSystemUserCreationForm()
	
	context = { 'form': form }

	return render(request, 'registration/register.html', context)

@unauthenticated_user_only
def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Successfully logged in!")
			return redirect('index')
		else:
			messages.info(request, 'Incorrect username or password!')
	
	context = {}
	return render(request, 'registration/login.html', context)

def logout_user(request):
	logout(request)
	return redirect('login')