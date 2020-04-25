from django.shortcuts import render
from background_task import background
from django.db.models import Count

from .models import TopAppliedJob, PeopleWhoAppliedThisAlsoApplied
from job_system_module.models import *

from django.db import connection
from django.core.paginator import Paginator

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
    print("New recommendations generated Successfully!!!")
    
@background(schedule=1)
def initialize_calculate_people_who_applied_this_also_applied():
    print("Starting job to create people who applied this also applied recommendations.")

    PeopleWhoAppliedThisAlsoApplied.objects.all().delete()
    jobs = Job.objects.all()

    paginated_jobs = Paginator(jobs, 1000)

    for page in range(1, paginated_jobs.num_pages + 1):
        for job in paginated_jobs.page(page).object_list:
            applicant_ids = job.jobapplication_set.all().values_list('user_id', flat=True)
            also_applied_jobs_with_counts = JobApplication.objects.filter(user_id__in=applicant_ids).exclude(job_id=job.id).values('job_id').annotate(applications_count=Count('job_id')).order_by('-applications_count')[:20]
            for applied_job_with_count in also_applied_jobs_with_counts:
                try:
                    also_applied_job = Job.objects.get(pk=applied_job_with_count['job_id'])
                    already_added_recommendation = PeopleWhoAppliedThisAlsoApplied.objects.filter(job=job, also_applied_job=also_applied_job).first()
                    if not already_added_recommendation:
                        also_applied_job_recommendation = PeopleWhoAppliedThisAlsoApplied(job=job, also_applied_job=also_applied_job, similarity=applied_job_with_count['applications_count'])
                        also_applied_job_recommendation.save()
                except Exception:
                        print('An minor error occurred while creating PeopleWhoAppliedThisAlsoApplied operation.')
    print("New recommendations generated Successfully!!!")