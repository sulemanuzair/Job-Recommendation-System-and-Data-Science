import pandas as pd
from constants import *
from constants import *
import numpy as np
from bs4 import BeautifulSoup as soup
from nltk.corpus import stopwords

job_files = [
       dataset_path + '/splitjobs/splitjobs/jobs1.tsv',
       dataset_path + '/splitjobs/splitjobs/jobs2.tsv',
       dataset_path + '/splitjobs/splitjobs/jobs3.tsv',
       dataset_path + '/splitjobs/splitjobs/jobs4.tsv',
       dataset_path + '/splitjobs/splitjobs/jobs5.tsv',
       dataset_path + '/splitjobs/splitjobs/jobs6.tsv',
       dataset_path + '/splitjobs/splitjobs/jobs7.tsv'
    ]


job_output_files = [
    dataset_path + '/splitjobs/splitjobs/jobs1_a.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs1_b.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs1_c.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs1_d.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs1_e.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs2_a.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs2_b.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs2_c.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs2_d.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs2_e.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs3_a.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs3_b.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs3_c.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs4_a.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs4_b.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs4_c.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs5_a.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs5_b.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs5_c.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs6_a.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs6_b.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs6_c.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs7_a.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs7_b.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs7_c.tsv'
]
FILE_DIVIDE_FACTOR_FOR_BIGGER_FILES = 5
FILE_DIVIDE_FACTOR_FOR_SMALLER_FILES = 3

output_file_index = 0
for file_number, file_name in enumerate(job_files):
    jobs = pd.read_csv(file_name, sep='\t', engine='python',  error_bad_lines=False)
    if file_number < 2:
        jobs_chunks = np.array_split(jobs, FILE_DIVIDE_FACTOR_FOR_BIGGER_FILES)
    else:
        jobs_chunks = np.array_split(jobs, FILE_DIVIDE_FACTOR_FOR_SMALLER_FILES)
    for jobs_chunk in jobs_chunks:
        jobs_chunk.to_csv(job_output_files[output_file_index], sep='\t', index=False)
        output_file_index = output_file_index + 1
    # For releasing memory
    del jobs
    del jobs_chunks
