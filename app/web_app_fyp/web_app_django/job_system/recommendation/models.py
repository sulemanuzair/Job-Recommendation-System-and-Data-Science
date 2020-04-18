from django.db import models
from job_system_module.models import *
# Create your models here.

class TopAppliedJob(models.Model):
	job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
	applications_count = models.IntegerField()
