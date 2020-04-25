# Product Association with lift, product that naturally occurs less gets more importance
from constants import *
import pandas as pd

job_applications_file = dataset_path + '/apps/apps.tsv'
#jobs_file = dataset_path + '/splitjobs/splitjobs/jobs1.tsv'
apps = pd.read_csv(job_applications_file, sep='\t')
#jobs = pd.read_csv(jobs_file, sep='\t')
print('Total jobs in this sample : ', apps.shape[0])
#187358
selected_job_application = apps.loc[apps['JobID'] == 187358].iloc[0:1, :]
print('Selected Job Application: ', selected_job_application)
#selected_job_application = apps.iloc[0:1, :]

# import  pdb; pdb.set_trace()
selected_user_id = selected_job_application.UserID.values.item(0)
selected_job_id = selected_job_application.JobID.values.item(0)

print('Selected with ', (selected_job_id))
jobs_with_count_applied = apps.JobID.value_counts()

job_applications_with_selected_job = apps.loc[apps['JobID'] == selected_job_id]
users_who_applied_selected_job = job_applications_with_selected_job.UserID

print('users_who_applied_selected_job', users_who_applied_selected_job)

jobs_applied_by_users_who_applied_selected_job = apps.loc[apps['UserID'].isin(users_who_applied_selected_job)]
#remove rows where user is selected_user

# Values can be sorted in ascending order
print('jobs_applied_by_users_who_applied_selected_job', jobs_applied_by_users_who_applied_selected_job.JobID.value_counts())
jobs_applied_by_users_who_applied_selected_job_with_their_counts_with_those_users = jobs_applied_by_users_who_applied_selected_job.JobID.value_counts()
ids_of_jobs_applied_by_users_who_applied_selected_job = jobs_applied_by_users_who_applied_selected_job.JobID.value_counts().index.values
# next line variable not being used
#ids_list_of_jobs_applied_by_users_who_applied_selected_job = jobs_applied_by_users_who_applied_selected_job.JobID.value_counts().index.tolist()
jobs_with_count_of_selected_jobs = jobs_with_count_applied.loc[jobs_with_count_applied.index.isin(ids_of_jobs_applied_by_users_who_applied_selected_job)]

#also need to apply some basic criteria, at least these many should have been applied
lifted_association = pd.Series()
for job_id, count_in_specific_users_of_applied_job in jobs_applied_by_users_who_applied_selected_job_with_their_counts_with_those_users.items():
    #assuming non zero entries
    general_count_of_applied_job = jobs_with_count_of_selected_jobs[job_id]
    lifted_association.at[job_id] = count_in_specific_users_of_applied_job/general_count_of_applied_job
lifted_association = lifted_association.sort_values(ascending=False)

print("top jobs ids with lifted association", lifted_association)