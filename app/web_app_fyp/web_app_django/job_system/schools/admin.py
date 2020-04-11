from django.contrib import admin

# Register your models here.
from .models import Course, Student

admin.site.site_header = 'Jobs System Admin Panel'
admin.site.site_title = 'Jobs System'
#admin.site.index_title = 'Jobs Index' #left unchanged to use system default

class StudentsInCourse(admin.TabularInline):
	model = Student
	extra = 1

class CourseWithStudents(admin.ModelAdmin):
	fieldsets = [
		(None,         { 'fields': ['name'] }),
		('Start Date', { 'fields': ['start_date'], 'classes': ['collapse']}),
	]

	inlines = [StudentsInCourse]

admin.site.register(Course, CourseWithStudents)
admin.site.register(Student)