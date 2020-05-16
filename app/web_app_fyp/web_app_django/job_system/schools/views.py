from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Course, Student 
# Create your views here.
from recommendation.views import *

def index(request):
	courses = Course.objects.all()
	context = {'courses': courses}
	#initialize_calculate_people_who_applied_this_also_applied()
	return render(request, 'schools/index.html', context)

def course(request, course_id):
	try:
		course = Course.objects.get(pk=course_id)
		not_this_course_students = Student.objects.exclude(course_id=course.id)
	except Course.DoesNotExist:
		raise Http404('Course does not exist')
	return render(request, 'schools/course.html', { 'course': course, 'not_this_course_students': not_this_course_students })

def enroll_student(request, course_id):
	course = get_object_or_404(Course, pk=course_id)
	try:
		student = Student.objects.exclude(course_id=course.id).get(pk=request.POST['student_id'])
	except(KeyError, Student.DoesNotExist):
		return render(request, 'schools/course.html', {
			'course': course,
			'error_message': "Custom error: Student not found",
		})
	else:
		student.course = course
		student.save()
		return HttpResponseRedirect(reverse('schools:course', args=(course.id,)))
