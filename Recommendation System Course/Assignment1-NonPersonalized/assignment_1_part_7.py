# Demographic
from constants import *
import pandas as pd

# job_applications_file = dataset_path + '/apps/apps_part.tsv'
# #jobs_file = dataset_path + '/splitjobs/splitjobs/jobs1.tsv'
# apps = pd.read_csv(job_applications_file, sep='\t')
# #jobs = pd.read_csv(jobs_file, sep='\t')
# print('Total jobs in this sample : ', apps.shape[0])
# selected_job_application = apps.loc[apps['JobID'] == 187358].iloc[0:1, :]
# print('Selected Job Application: ', selected_job_application)
# #selected_job_application = apps.iloc[0:1, :]
#
# # import  pdb; pdb.set_trace()
# selected_user_id = selected_job_application.UserID.values.item(0)
# selected_job_id = selected_job_application.JobID.values.item(0)
#
# print('Selected with ', (selected_job_id))
# jobs_with_count_applied = apps.JobID.value_counts()
#
# job_applications_with_selected_job = apps.loc[apps['JobID'] == selected_job_id]
# users_who_applied_selected_job = job_applications_with_selected_job.UserID
#
# print(users_who_applied_selected_job)
#
# jobs_applied_by_users_who_applied_selected_job = apps.loc[apps['UserID'].isin(users_who_applied_selected_job)]
# #remove rows where user is selected_user
#
# # Values can be sorted in ascending order
# print(jobs_applied_by_users_who_applied_selected_job.JobID.value_counts())
#
# # print("Top jobs applied by people who applied this job", jobs.loc[jobs['JobID'] == 130364])


# Using database and SQL queries to fetch jobs
import pymysql
domain = 'localhost'
username = 'root'
password = ''
db_name = 'jobs_system'
table_name = 'jobs'
db = pymysql.connect(domain, username, password, db_name)

cursor = db.cursor()


try:
    sql = 'select count(*) from job_applications ' \
          'join jobs on jobs.id < 5000 and job_applications.job_id < 5000 and job_applications.job_id = jobs.id ' \
          'join users on users.id = job_applications.user_id ' \
          'where jobs.id < 5000 and job_applications.job_id < 5000 and end_date IS NOT NULL and application_date > end_date and currently_employed = false;'

    cursor.execute(sql)
    jobs = cursor.fetchall()
    for row in jobs:
        print('Number of time unemployed people applied on ended job: ', row)

    sql = 'select count(*) from job_applications ' \
          'join jobs on jobs.id < 5000 and job_applications.job_id < 5000 and job_applications.job_id = jobs.id ' \
          'join users on users.id = job_applications.user_id ' \
          'where jobs.id < 5000 and job_applications.job_id < 5000 and end_date IS NOT NULL and application_date > end_date and currently_employed = true;'

    cursor.execute(sql)
    jobs = cursor.fetchall()
    for row in jobs:
        print('Number of time employed people applied on ended job: ', row)



except:
    print('Error: Error in SQL data fetch')
db.close()


