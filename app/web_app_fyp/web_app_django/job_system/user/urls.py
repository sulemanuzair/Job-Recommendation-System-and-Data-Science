from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
	path('job_history', views.job_history, name='job_history'),
	path('job_application_history', views.job_application_history, name='job_application_history')
]