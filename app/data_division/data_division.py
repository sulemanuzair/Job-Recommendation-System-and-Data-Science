import pandas as pd
from constants import *
fraction_of_data = 0.25

filesInputNames = [
                   # '../apps/apps.tsv',
                   # '../splitjobs/splitjobs/jobs1.tsv',
                   dataset_path + '/splitjobs/splitjobs/jobs2.tsv'#,
                   # '../splitjobs/splitjobs/jobs3.tsv',
                   # '../splitjobs/splitjobs/jobs4.tsv',
                   # '../splitjobs/splitjobs/jobs5.tsv',
                   # '../splitjobs/splitjobs/jobs6.tsv',
                   # '../splitjobs/splitjobs/jobs7.tsv',
                   # '../users/users.tsv',
                   # '../user_history/user_history.tsv'
                  ]
filesOutputNames = [
                    # '../apps/apps_part.tsv',
                    # '../splitjobs/splitjobs/jobs1_part.tsv',
                    dataset_path + '/splitjobs/splitjobs/jobs2_part.tsv'#,
                    # '../splitjobs/splitjobs/jobs3_part.tsv',
                    # '../splitjobs/splitjobs/jobs4_part.tsv',
                    # '../splitjobs/splitjobs/jobs5_part.tsv',
                    # '../splitjobs/splitjobs/jobs6_part.tsv',
                    # '../splitjobs/splitjobs/jobs7_part.tsv',
                    # '../users/users_part.tsv',
                    # '../user_history/user_history_part.tsv'
                   ]

for i in range(len(filesInputNames)):
    data = pd.read_csv(filesInputNames[i], sep='\t', engine='python',  error_bad_lines=False)
    # data = data.sample(frac=fraction_of_data) #for random division
    print(len(data))
    data = data[0:int(len(data)*fraction_of_data)]
    data.to_csv(filesOutputNames[i], sep='\t', index=False)
