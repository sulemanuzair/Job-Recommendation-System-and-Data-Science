from constants import *
import pandas as pd
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

JOBS_COLUMNS_FOR_STRING_PREPROCESSING = ['Title', 'Description', 'Requirements']
JOBS_COLUMNS_WITH_HTML = ['Description', 'Requirements']
REQUIREMENT_COLUMN = 'Requirements'
PUNCTUATION = '!"”#$¢™%&\'()*+,-./:;<=>?@[\\]^_`{}~|'#`∑` is not present here
PUNCTUATION_CHARACTERS = str.maketrans(dict.fromkeys(PUNCTUATION, ' '))

stop_words = stopwords.words('english')
requirements_filter_string = "Please refer to the Job Description to view the requirements for this job"
file_name = dataset_path + '/splitjobs/splitjobs/jobs2_part.tsv'
jobs = pd.read_csv(file_name, sep='\t')

for column in JOBS_COLUMNS_FOR_STRING_PREPROCESSING:
    if column == REQUIREMENT_COLUMN:
        jobs[column] = jobs[column].replace(requirements_filter_string, "")
    jobs[column] = jobs[column].str.lower()
    if column in JOBS_COLUMNS_WITH_HTML:
        jobs[column] = [soup(str(text), "html.parser").get_text() for text in jobs[column]]
        jobs[column].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r|â|€|œ|�"], value=[" ", " "], regex=True, inplace=True)
    jobs[column] = ('∑'.join(str(v) for v in jobs[column].tolist()).translate(PUNCTUATION_CHARACTERS).split('∑'))
    jobs[column] = jobs[column].str.split()

    jobs[column] = jobs[column].apply(lambda x: [item for item in x if item not in stop_words])
    merged_strings = []
    for index, row in jobs.iterrows():
        merged_string = ' '.join((row[column]))
        merged_strings.append(merged_string)
    jobs[column] = pd.Series(merged_strings)

# for checking data on console
JOBS_ROWS_FOR_ANALYZING = 15
show_job_details_console(jobs.sample(JOBS_ROWS_FOR_ANALYZING), show_option='individual_attribute', show_all_cols=False, cols=JOBS_COLUMNS_FOR_STRING_PREPROCESSING)
show_job_details_console(jobs[0:JOBS_ROWS_FOR_ANALYZING], show_option='default', show_all_cols=False, cols=JOBS_COLUMNS_FOR_STRING_PREPROCESSING)

file_name_to_save = get_file_name_to_save(file_name)
jobs.to_csv(file_name_to_save, sep='\t', index=False)
