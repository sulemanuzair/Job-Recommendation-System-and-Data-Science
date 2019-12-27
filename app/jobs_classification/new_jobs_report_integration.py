from constants import *
import pandas as pd

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

report_file_sector = reports_path + "/new_jobs_sector.csv"
report_file_organization = reports_path + "/new_jobs_organization.csv"
new_jobs_file = dataset_path + "/jobs_for_classification/us_jobs.csv"

jobs = pd.read_csv(new_jobs_file)
sectors = pd.read_csv(report_file_sector, header=None)
organizations = pd.read_csv(report_file_organization, header=None)

#print(jobs.loc[jobs['sector'].isnull()])

sectors = sectors.loc[:, 0:2]
organizations = organizations.loc[:, 0:2]

sectors = sectors.loc[sectors[2] == 1]
organizations = organizations.loc[organizations[2] == 1]

sectors = sectors[0].tolist()
organizations = organizations[0].tolist()

#hash for faster search
sectors_hash = {sectors[i]: sectors[i] for i in range(0, len(sectors))}
organizations_hash = {organizations[i]: organizations[i] for i in range(0, len(organizations))}

print(len(jobs.loc[jobs['sector'].isin(sectors_hash)]))
print(len(jobs.loc[jobs['organization'].isin(organizations_hash)]))
print(len(jobs.loc[jobs['organization'].isin(organizations_hash) | jobs['sector'].isin(sectors_hash)]))

#jobs = jobs.loc[jobs['organization'].isin(organizations_hash) | jobs['sector'].isin(sectors_hash)]
jobs = jobs.loc[jobs['sector'].isin(sectors_hash)]

jobs.to_csv(dataset_path + '/jobs_for_classification/us_jobs_sector_or_organization.csv')

