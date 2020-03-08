from django.db import models

# Create your models here.
# Assumption here, one student has only one course
class Course(models.Model):
	name = models.CharField(max_length=200)
	start_date = models.DateTimeField('Start Date')

class Student(models.Model):
	name   = models.CharField(max_length=200)
	age    = models.IntegerField
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

