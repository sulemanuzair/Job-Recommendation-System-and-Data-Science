from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Job, User, JobApplication, UserHistory

@login_required(login_url='login')
def index(request):
	jobs = Job.objects.all()
	page = request.GET.get('page')
	
	paginator = Paginator(jobs, 15)
	jobs = paginator.get_page(page)

	max1 = jobs.paginator.num_pages
	min1 = 0
	curr = jobs.number
	
	min2 = max(0, curr - 5)
	max2 = min(max1, curr + 5)
	yes = range(min2, max2)
	context = {'jobs': jobs, 'yes': yes}
	return render(request, 'job_system/index.html', context)