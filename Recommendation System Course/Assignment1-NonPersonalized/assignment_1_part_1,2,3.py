from constants import *
import pandas as pd
import pandasql as ps

job_applications_file = dataset_path + '/apps/apps.tsv'
apps = pd.read_csv(job_applications_file, sep='\t')

print('Total jobs in this sample : ', apps.shape[0])
print('Jobs with how many times they have been applied : \n', apps.JobID.value_counts())

top_3_most_applied_jobs = apps.JobID.value_counts()[0:3].keys().values[0:3]
print('Top 3 Most Applied Jobs : \n', apps.JobID.value_counts()[0:3])

# Using database and SQL queries to fetch jobs
import pymysql
domain = 'localhost'
username = 'root'
password = ''
db_name = 'jobs_system'
table_name = 'jobs'
db = pymysql.connect(domain, username, password, db_name)

cursor = db.cursor()
sql_fetch_jobs = "SELECT * " \
                 "FROM %s " \
                 "WHERE id = '%d' or id = '%d' or id = '%d';" % (table_name, top_3_most_applied_jobs.item(0), top_3_most_applied_jobs.item(1), top_3_most_applied_jobs.item(2))
print(sql_fetch_jobs)
try:
    cursor.execute(sql_fetch_jobs)
    jobs = cursor.fetchall()
    for row in jobs:
        print(row[2])
        print(row)
except:
    print('Error: Error in SQL data fetch')
db.close()



