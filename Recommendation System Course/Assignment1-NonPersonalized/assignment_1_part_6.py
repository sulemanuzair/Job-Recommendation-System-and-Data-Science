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


#sql_fetch_jobs = "SELECT title " \
#                 "FROM %s " \
#                "WHERE job_id = %d or job_id = %d or job_id = %d;" % (table_name, 130364, 65413, 98665)
#print(sql_fetch_jobs)
try:
    sql_users_already_employed = 'select count(id) from users where currently_employed = TRUE;'
    sql_users_not_employed = 'select count(id) from users where currently_employed = false;'
    cursor.execute(sql_users_already_employed)
    jobs = cursor.fetchall()
    for row in jobs:
        print(row)
        users_count_employed = row[0]

    cursor.execute(sql_users_not_employed)
    jobs = cursor.fetchall()
    for row in jobs:
        print(row)
        users_count_not_employed = row[0]
    sql_job_application_count_for_employed_users = 'select count(*) from job_applications ' \
                                                   'join users on job_applications.user_id = users.id ' \
                                                   'where currently_employed = true;'
    print(sql_job_application_count_for_employed_users)
    cursor.execute(sql_job_application_count_for_employed_users)
    jobs = cursor.fetchall()
    for row in jobs:
        print(row)
        job_applications_count_by_employed_users = row[0]

    sql_job_application_count_for_unemployed_users = 'select count(*) from job_applications ' \
                                                   'join users on job_applications.user_id = users.id ' \
                                                   'where currently_employed = false;'
    print(sql_job_application_count_for_unemployed_users)
    cursor.execute(sql_job_application_count_for_unemployed_users)
    jobs = cursor.fetchall()
    for row in jobs:
        print(row)
        job_applications_count_by_unemployed_users = row[0]

    print("Jobs applied per each employed user", job_applications_count_by_employed_users / users_count_employed)
    print("Jobs applied per each unemployed user", job_applications_count_by_unemployed_users / users_count_not_employed)
except:
    print('Error: Error in SQL data fetch')
db.close()


