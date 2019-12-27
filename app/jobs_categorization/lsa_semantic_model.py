import sys
sys.path.append('G:\Semester 8\FYP2')
from constants import *
import pandas as pd
from nltk import word_tokenize
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 500)

# Load the library with the CountVectorizer method
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import seaborn as sns
#import warnings
#warnings.simplefilter("ignore", DeprecationWarning)
from sklearn.decomposition import LatentDirichletAllocation as LDA

jobs_file = dataset_path + '/splitjobs/splitjobs/jobs2_partS.tsv'
jobs = pd.read_csv(jobs_file, sep='\t')
jobs_size = len(jobs)

#JOBS_COLUMNS_TEXT = ['Title', 'Description', 'Requirements']
col_constant = 2
if col_constant == 0:
    use_rows = 0.5
    JOBS_COLUMNS_TEXT = ['Title']
elif col_constant == 1:
    use_rows = 0.1
    JOBS_COLUMNS_TEXT = ['Description']
else:
    use_rows = 0.5
    JOBS_COLUMNS_TEXT = ['Requirements']

jobs = jobs[0:int(use_rows * jobs_size)]
# Helper function
def plot_10_most_common_words(count_data, count_vectorizer):
    import matplotlib.pyplot as plt
    words = count_vectorizer.get_feature_names()
    total_counts = np.zeros(len(words))
    for t in count_data:
        total_counts += t.toarray()[0]

    count_dict = (zip(words, total_counts))
    count_dict = sorted(count_dict, key=lambda x: x[1], reverse=True)[0:10]
    words = [w[0] for w in count_dict]
    counts = [w[1] for w in count_dict]
    x_pos = np.arange(len(words))

    plt.figure(2, figsize=(15, 15 / 1.6180))
    plt.subplot(title='10 most common words')
    sns.set_context("notebook", font_scale=1.25, rc={"lines.linewidth": 2.5})
    sns.barplot(x_pos, counts, palette='husl')
    plt.xticks(x_pos, words, rotation=90)
    plt.xlabel('words')
    plt.ylabel('counts')
    plt.show()

# Helper function
def print_topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print("\nTopic #%d:" % topic_idx)
        print(" ".join([words[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))

for column in JOBS_COLUMNS_TEXT:
    # Initialise the count vectorizer with the English stop words
    count_vectorizer = CountVectorizer(stop_words='english')
    jobs[column] = jobs[column].fillna("")

    count_data = count_vectorizer.fit_transform(jobs[column])
    #plot_10_most_common_words(count_data, count_vectorizer)

    # Tweak the two parameters below
    number_topics = 100
    number_words = 15
    # Create and fit the LDA model
    lda = LDA(n_components=number_topics, n_jobs=1, learning_decay=0.85, learning_offset=40, max_iter=25, evaluate_every=0.01, max_doc_update_iter=300)
    #print ('count_Data', count_data)
    lda.fit(count_data)
    # Print the topics found by the LDA model
    print("Topics found via LDA:")
    print_topics(lda, count_vectorizer, number_words)











# Import the wordcloud library
#from wordcloud import WordCloud
# Join the different processed titles together.
#long_string = ','.join(list(papers['paper_text_processed'].values))
# Create a WordCloud object
#wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')
# Generate a word cloud
#wordcloud.generate(long_string)
# Visualize the word cloud
#wordcloud.to_image()