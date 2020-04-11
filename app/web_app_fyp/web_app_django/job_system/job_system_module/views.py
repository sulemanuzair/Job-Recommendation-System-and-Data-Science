from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Job, User, JobApplication, UserHistory
from .filters import JobsFilter

@login_required(login_url='login')
def index(request):
	jobs = Job.objects.filter(id__lt=10000) #[0:200]
	jobs_filter = JobsFilter(request.GET, queryset=jobs)
	jobs = jobs_filter.qs.prefetch_related()

	app1 = jobs.first().jobapplication_set
	
	page = request.GET.get('page')
	paginator = Paginator(jobs, 15)
	jobs = paginator.get_page(page)

	total_pages = jobs.paginator.num_pages
	min_page = 1
	curr_page = jobs.number
	page_range = 5 #twice of this
	lower_page_limit = max(min_page, curr_page - page_range)
	upper_page_limit = min(total_pages, curr_page + page_range)
	pages_range = range(lower_page_limit, upper_page_limit)

	context = { 'jobs': jobs, 'pages_range': pages_range, 'jobs_filter': jobs_filter }
	return render(request, 'job_system/index.html', context)