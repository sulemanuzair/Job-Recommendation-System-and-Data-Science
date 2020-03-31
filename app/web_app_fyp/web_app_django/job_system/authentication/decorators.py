from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user_only(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('index')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups().all().first().name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are authorized to view this page')
		return wrapper_func
	return decorator

def applicant_to_root(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all().first().name

		if group == 'applicant':
			return redirect('/')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func
