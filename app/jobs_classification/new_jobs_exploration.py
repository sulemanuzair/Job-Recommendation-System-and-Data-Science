from constants import *
from sklearn import svm
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn import tree
from gensim.models import Word2Vec

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
stop_words = set(stopwords.words('english'))
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 500)

input_file = dataset_path + "/jobs_for_classification/us_jobs.csv"

jobs = pd.read_csv(input_file)
#print(jobs.describe())
#jobs = jobs[0:3000]
PUNCTUATION = '!"”#$¢™%&\'()*+,-./:;<=>?@[\\]^_`{}~|'#`∑` is not present here
PUNCTUATION_CHARACTERS = str.maketrans(dict.fromkeys(PUNCTUATION, ' '))
stop_words = stopwords.words('english')
label_encoder = LabelEncoder()

# jobs['job_title_description'] = jobs['job_title'] + jobs['job_description']
# #dataframe["period"] = dataframe["Year"].map(str) + dataframe["quarter"]
#
# column = 'job_title_description'
# label_column = 'sector'
# jobs[column] = jobs[column].str.lower()
# jobs[column] = ('∑'.join(str(v) for v in jobs[column].tolist()).translate(PUNCTUATION_CHARACTERS).split('∑'))
# jobs[column] = jobs[column].str.split()
# jobs[column] = jobs[column].apply(lambda x: [item for item in x if item not in stop_words])
#
# merged_strings = []
# for index, row in jobs.iterrows():
#     merged_string = ' '.join((row[column]))
#     merged_strings.append(merged_string)
# jobs[column] = pd.Series(merged_strings)


print((jobs['sector'].value_counts()))
print((jobs['organization'].value_counts()))

#jobs['sector'].value_counts().to_csv(reports_path + '/new_jobs_sector.csv')
jobs['sector'].value_counts().to_csv(reports_path + '/new_jobs_sector.csv')
jobs['organization'].value_counts().to_csv(reports_path + '/new_jobs_organization.csv')

#print(jobs.groupby('sector').count())