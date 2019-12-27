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


print(len(sectors), sectors)
print(len(organizations), organizations)
print(type(sectors))

with open(reports_path + '/sectors.csv', "w") as outfile:
    for entries in sectors:
        outfile.write(entries)
        outfile.write("\n")

with open(reports_path + '/organizations.csv', "w") as outfile:
    for entries in organizations:
        outfile.write(entries)
        outfile.write("\n")

