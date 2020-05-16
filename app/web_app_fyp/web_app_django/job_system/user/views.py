from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def job_history(request):
	user_detail = request.user.user_set.first()
	job_histories = None
	if user_detail:
		job_histories = user_detail.userhistory_set.all()	
	return render(request, 'user/job_history.html', { 'job_histories': job_histories })


@login_required(login_url='login')
def job_application_history(request):
	user_detail = request.user.user_set.first()
	job_application_histories = None
	if user_detail:
		job_application_histories = user_detail.jobapplication_set.all()	
	return render(request, 'user/job_application_history.html', { 'job_application_histories': job_application_histories })
