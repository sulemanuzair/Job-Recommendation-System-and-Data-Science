from django.urls import path
from . import views

app_name = 'schools'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:course_id>/course', views.course, name='course'),
	path('<int:course_id>/enroll_student', views.enroll_student, name='enroll_student')
]