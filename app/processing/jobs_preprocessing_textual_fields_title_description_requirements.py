from constants import *
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
from nltk.corpus import stopwords

def show_job_details_console(jobs, show_option= 'default', show_all_cols=True, cols = []):
    if show_all_cols:
        cols = jobs.columns
    if show_option == 'default':
        for index, row in jobs.iterrows():
            for column in cols:
                print(column + ' :', row[column])
            print("")
    elif show_option == 'individual_attribute':
        for column in cols:
            for row in jobs[column]:
                print(column + ' :', row)
            print("")

def get_file_name_to_save(file_name):
    file_name_parts = file_name.split('.')
    file_name_parts[-2] += "S"
    file_name = '.'.join(file_name_parts)
    return file_name

job_files = [
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

job_output_files = [
    dataset_path + '/splitjobs/splitjobs/jobs1_a_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs1_b_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs1_c_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs1_d_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs1_e_processed.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs2_a_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs2_b_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs2_c_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs2_d_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs2_e_processed.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs3_a_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs3_b_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs3_c_processed.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs4_a_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs4_b_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs4_c_processed.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs5_a_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs5_b_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs5_c_processed.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs6_a_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs6_b_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs6_c_processed.tsv',

    dataset_path + '/splitjobs/splitjobs/jobs7_a_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs7_b_processed.tsv',
    dataset_path + '/splitjobs/splitjobs/jobs7_c_processed.tsv'
    ]

PANDAS_DIVIDE_JOBS = 50
JOBS_COLUMNS_FOR_STRING_PREPROCESSING = ['Title', 'Description', 'Requirements']
JOBS_COLUMNS_WITH_HTML = ['Description', 'Requirements']
REQUIREMENT_COLUMN = 'Requirements'
PUNCTUATION = '!"”#$¢™%&\'()*+,-./:;<=>?@[\\]^_`{}~|'#`∑` is not present here
PUNCTUATION_CHARACTERS = str.maketrans(dict.fromkeys(PUNCTUATION, ' '))
ORIGINAL = '_original'

stop_words = stopwords.words('english')
requirements_filter_string = "Please refer to the Job Description to view the requirements for this job"

for file_number, file_name in enumerate(job_files):
    jobs = pd.read_csv(file_name, sep='\t', engine='python',  error_bad_lines=False)
    jobs_chunks = np.array_split(jobs, PANDAS_DIVIDE_JOBS)

    for jobs_chunk in jobs_chunks:
        for column in JOBS_COLUMNS_FOR_STRING_PREPROCESSING:
            jobs_chunk[column + ORIGINAL] = jobs_chunk[column]
            if column == REQUIREMENT_COLUMN:
                jobs_chunk[column] = jobs_chunk[column].replace(requirements_filter_string, "")
            jobs_chunk[column] = jobs_chunk[column].str.lower()
            if column in JOBS_COLUMNS_WITH_HTML:
                jobs_chunk[column] = [soup(str(text), "html.parser").get_text() for text in jobs_chunk[column]]
                jobs_chunk[column].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r|â|€|œ|�"], value=[" ", " "], regex=True, inplace=True)

            jobs_chunk[column] = ('∑'.join(str(v) for v in jobs_chunk[column].tolist()).translate(PUNCTUATION_CHARACTERS).split('∑'))
            jobs_chunk[column] = jobs_chunk[column].str.split()

            jobs_chunk[column] = jobs_chunk[column].apply(lambda x: [item for item in x if item not in stop_words])
            merged_strings = []
            for index, row in jobs_chunk.iterrows():
                merged_string = ' '.join(row[column])
                merged_strings.append(merged_string)
            jobs_chunk[column] = merged_strings
    jobs = pd.concat(jobs_chunks)
    # for checking data on console
    # JOBS_ROWS_FOR_ANALYZING = 15
    # show_job_details_console(jobs.sample(JOBS_ROWS_FOR_ANALYZING), show_option='individual_attribute', show_all_cols=False, cols=JOBS_COLUMNS_FOR_STRING_PREPROCESSING)
    # show_job_details_console(jobs[0:JOBS_ROWS_FOR_ANALYZING], show_option='default', show_all_cols=False, cols=JOBS_COLUMNS_FOR_STRING_PREPROCESSING)

    file_name_to_save = job_output_files[file_number]
    jobs.to_csv(file_name_to_save, sep='\t', index=False)
    del jobs
    del jobs_chunks