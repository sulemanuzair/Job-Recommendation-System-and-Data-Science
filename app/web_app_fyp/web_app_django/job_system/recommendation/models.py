from django.db import models
from job_system_module.models import *
# Create your models here.

class TopAppliedJob(models.Model):
	job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
	applications_count = models.IntegerField()

class PeopleWhoAppliedThisAlsoApplied(models.Model):
	job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job')
	also_applied_job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='also_applied_job')
	similarity = models.DecimalField(max_digits=8, decimal_places=2)