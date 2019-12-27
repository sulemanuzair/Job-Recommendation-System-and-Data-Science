from constants import *
from sklearn import svm
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn import tree
from gensim.models import Word2Vec

import pandas as pd
import numpy as npf
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_scorecfv



from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
stop_words = set(stopwords.words('english'))
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 500)

#vectorizer = HashingVectorizer(n_features=100000)
vectorizer = TfidfVectorizer()
#vectorizer = Word2Vec()
input_file = dataset_path + "/jobs_for_classification/us_jobs_sector_or_organization.csv"

jobs = pd.read_csv(input_file)
jobs = jobs[0:5000]
#jobs.dropna(subset=['sector'], inplace=True) #jobs[np.isfinite(jobs['sector'])]
PUNCTUATION = '!"”#$¢™%&\'()*+,-./:;<=>?@[\\]^_`{}~|'#`∑` is not present here
PUNCTUATION_CHARACTERS = str.maketrans(dict.fromkeys(PUNCTUATION, ' '))
stop_words = stopwords.words('english')
label_encoder = LabelEncoder()

jobs['job_title_description'] = jobs['job_title'] + jobs['job_description']
#dataframe["period"] = dataframe["Year"].map(str) + dataframe["quarter"]

column = 'job_title_description'
label_column = 'sector'
jobs[column] = jobs[column].str.lower()
jobs[column] = ('∑'.join(str(v) for v in jobs[column].tolist()).translate(PUNCTUATION_CHARACTERS).split('∑'))
jobs[column] = jobs[column].str.split()
jobs[column] = jobs[column].apply(lambda x: [item for item in x if item not in stop_words])

merged_strings = []
for index, row in jobs.iterrows():
    merged_string = ' '.join((row[column]))
    merged_strings.append(merged_string)
jobs[column] = pd.Series(merged_strings)

labels = label_encoder.fit_transform(jobs[label_column].apply(str))
#dividing data into train and test
training_jobs, test_jobs, training_labels, test_labels = train_test_split(jobs, labels, test_size = 0.2, random_state = None)


training_jobs_description = vectorizer.fit_transform(training_jobs[column].array)
test_jobs_description = vectorizer.transform(test_jobs[column].array)

#svm = tree.DecisionTreeClassifier()
#svm = svm.SVC()
#svm = svm.LinearSVC()#(max_iter=20000)  # SVR(C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma='auto',
#svm = MLPClassifier(hidden_layer_sizes=10, alpha=0.01)#hidden_layer_sizes=1000, alpha=0.005, activation='logistic' )
#svm = MLPClassifier()
svm = RandomForestClassifier(n_estimators=100)

svm = svm.fit(training_jobs_description, training_labels)

predicted_training_labels = svm.predict(training_jobs_description)
predicted_test_labels = svm.predict(test_jobs_description)

print("Training Accuracy : ", accuracy_score(training_labels, predicted_training_labels))
print("Test Accuracy : ", accuracy_score(test_labels, predicted_test_labels))



