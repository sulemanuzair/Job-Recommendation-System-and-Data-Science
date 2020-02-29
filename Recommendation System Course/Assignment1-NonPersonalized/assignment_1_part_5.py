#i dont know what happened in this, definitely something is wrong
#we found the corelation of job at position 1 with all other jobs

from constants import *
import pandas as pd
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

job_applications_file = dataset_path + '/apps/apps_part.tsv'
jobs_file = dataset_path + '/splitjobs/splitjobs/jobs2_partS.tsv'
apps = pd.read_csv(job_applications_file, sep='\t')
jobs = pd.read_csv(jobs_file, sep='\t')

jobs = jobs.iloc[0:500, 0:4]
jobs = jobs.apply(LabelEncoder().fit_transform)
result = jobs.corrwith(jobs.iloc[1], axis=1, method='pearson')
print(result)

