from django.db import models
from django.contrib.auth.models import User as AuthUser

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    window_id = models.IntegerField()
    split = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    degree_type = models.CharField(max_length=100)
    major = models.CharField(max_length=5000)
    graduation_date = models.DateTimeField()
    work_history_count = models.IntegerField()
    total_years_experience = models.FloatField()
    currently_employed = models.BooleanField()
    managed_others = models.BooleanField()
    managed_how_many = models.IntegerField()
    auth_user = models.ForeignKey(AuthUser, on_delete=models.SET_NULL, null=True)   

    class Meta:
        db_table = 'users'

class Job(models.Model):
    id = models.IntegerField(primary_key=True)
    window_id = models.IntegerField()
    title = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    requirement = models.CharField(max_length=5000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip5 = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    title_original = models.CharField(max_length=5000)
    description_original = models.CharField(max_length=5000)
    requirements_original = models.CharField(max_length=5000)

    class Meta:
        db_table = 'jobs'
    def __str__(self):
        return self.title

class JobApplication(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    window_id = models.IntegerField()
    split = models.CharField(max_length=20)
    application_date = models.DateTimeField()
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'job_applications'

class UserHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    window_id = models.IntegerField()
    split = models.CharField(max_length=20)
    sequence = models.IntegerField()
    job_title = models.CharField(max_length=5000)

    class Meta:
        db_table = 'user_histories'

