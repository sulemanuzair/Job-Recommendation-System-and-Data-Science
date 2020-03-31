from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import Job, User, JobApplication, UserHistory

def index(request):
	jobs = Job.objects.all()[0:100]
	authenticated = request.user.is_authenticated
	context = {'jobs': jobs, 'authenticated' : authenticated}
	return render(request, 'job_system/index.html', context)