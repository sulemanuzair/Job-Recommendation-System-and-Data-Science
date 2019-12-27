# looks like data summarization after preprocessing
from collections import Counter
from constants import *

import pandas as pd
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer


file_name = dataset_path + '/splitjobs/splitjobs/jobs2_partS.tsv'
jobs = pd.read_csv(file_name, sep='\t')

JOBS_COLUMNS_TEXT = ['Title', 'Description', 'Requirements']
for column in JOBS_COLUMNS_TEXT:
    jobs[column] = jobs[column].fillna("")
    ngram_vectorizer = CountVectorizer(analyzer='word', tokenizer=word_tokenize, ngram_range=(1, 1), min_df=1)
    X = ngram_vectorizer.fit_transform(jobs[column])
    vocab = list(ngram_vectorizer.get_feature_names())

    counts = X.sum(axis=0).A1
    freq_distribution = Counter(dict(zip(vocab, counts)))

    words_count = freq_distribution.most_common()
    output_file = reports_path + '/Jobs_' + column + '_Tokens_Info_25percent.csv'

    errors_in_writing_file = 0
    with open(output_file, "w") as outfile:
        for entries in words_count:
            try:
                outfile.write(str(("" + str(entries[0]) + ',' + str(entries[1]))))
                outfile.write("\n")
            except:
                errors_in_writing_file = errors_in_writing_file + 1

    print(column + " : Errors in file writing : ", errors_in_writing_file)