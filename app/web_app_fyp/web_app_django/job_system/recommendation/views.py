from django.shortcuts import render
from background_task import background

from .models import TopAppliedJob
from job_system_module.models import *

from django.db import connection

@background(schedule=1)
def calculate_top_applied_jobs():
    
    print("Starting job to create top job recommendations.")
    cursor = connection.cursor()
    cursor.execute("select job_id, count(user_id) as apps from job_applications where job_id > 6 group by job_id ORDER BY apps DESC limit 25;")
    rows = cursor.fetchall()

    print("Deleting previous recommendations.")
    TopAppliedJob.objects.all().delete()
    for job_and_app_count in rows:
        job = Job.objects.get(pk=job_and_app_count[0])
        top_applied_job = TopAppliedJob(job=job, applications_count=job_and_app_count[1])
        top_applied_job.save()
    print("New recommendations generated.")
    