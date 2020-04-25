from django.urls import path
from . import views

app_name = 'job_system_module'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:job_id>', views.show, name='show')
]