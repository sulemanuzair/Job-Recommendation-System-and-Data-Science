#summarization type after pre-processing for further processing
from constants import *
import pandas as pd
from nltk import word_tokenize
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 500)

words_file = reports_path + '/Jobs_Title_Tokens_Info_25percent.csv'
words = pd.read_csv(words_file)
words = words[['Word', 'Count', 'Type']]

jobs_file = dataset_path + '/splitjobs/splitjobs/jobs2_partS.tsv'
jobs = pd.read_csv(jobs_file, sep='\t')

seniority_words = words[words.Type == 1]
seniority_words_hash = {}
for index, word in seniority_words.iterrows():
    seniority_words_hash[word.Word] = [0] * len(jobs)

tokens_arrays = jobs['Title'].apply(word_tokenize)

row_number = 0
for tokens in tokens_arrays:
    for token in tokens:
        if token in seniority_words_hash:
            seniority_words_hash[token].insert(row_number, 1)
    row_number = row_number + 1


jobs_seniority_words = pd.DataFrame()
jobs_seniority_words['Title'] = jobs.Title
jobs_seniority_words['Description'] = jobs.Description

for each in seniority_words_hash:
    jobs_seniority_words[each] = pd.Series(seniority_words_hash[each])

jobs_seniority_words.to_csv(results_path + '/JobsCategorization/seniority_tokens_with_description.csv', index=False)