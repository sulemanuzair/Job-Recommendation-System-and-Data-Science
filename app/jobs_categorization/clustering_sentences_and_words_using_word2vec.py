#The code in this file is for clustering on the basis of text (tries)

#
# #step 1
# from gensim.models import Word2Vec
# sentences = [['this', 'is', 'the', 'good', 'machine', 'learning', 'book'],
#             ['this', 'is',  'another', 'book'],
#             ['one', 'more', 'book'],
#             ['this', 'is', 'the', 'new', 'post'],
#                         ['this', 'is', 'about', 'machine', 'learning', 'post'],
#             ['and', 'this', 'is', 'the', 'last', 'post']]
# model = Word2Vec(sentences, min_count=1)
#
#
#
# #step 2
# print (model.wv.similarity('this', 'is'))
# print (model.wv.similarity('post', 'book'))
# #output -0.0198180344218
# #output -0.079446731287
# print (model.wv.most_similar(positive=['machine'], negative=[], topn=2))
# #output: [('new', 0.24608060717582703), ('is', 0.06899910420179367)]
# print (model.wv['the'])
# #output [-0.00217354 -0.00237131  0.00296396 ...,  0.00138597  0.00291924  0.00409528]
#
#
# #step 3
# print (list(model.wv.vocab))
# print (len(list(model.wv.vocab)))
#
#
# #step4
# X = model.wv[model.wv.vocab]
#
# #step5
#
# from nltk.cluster import KMeansClusterer
# import nltk
# NUM_CLUSTERS=3
# kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25)
# assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
# print (assigned_clusters)
#
# #step6
# words = list(model.wv.vocab)
# for i, word in enumerate(words):
#     print (word + ":" + str(assigned_clusters[i]))
#
# #step7 clustering scikit
# from sklearn import cluster
# from sklearn import metrics
#
# kmeans = cluster.KMeans(n_clusters=NUM_CLUSTERS)
# kmeans.fit(X)
#
# labels = kmeans.labels_
# centroids = kmeans.cluster_centers_
#
# print("Cluster id labels for inputted data")
# print(labels)
# print("Centroids data")
# print(centroids)
#
# print(
#     "Score (Opposite of the value of X on the K-means objective which is Sum of distances of samples to their closest cluster center):")
# print(kmeans.score(X))
#
# silhouette_score = metrics.silhouette_score(X, labels, metric='euclidean')
#
# print("Silhouette_score: ")
# print(silhouette_score)




#2nd experiment
from constants import *
from gensim.models import Word2Vec

from nltk.cluster import KMeansClusterer
import nltk
import numpy as np

from sklearn import cluster
from sklearn import metrics
import pandas as pd
from nltk import word_tokenize

# training data
sentences = [['this', 'is', 'the', 'one', 'good', 'machine', 'learning', 'book'],
             ['this', 'is', 'another', 'book'],
             ['one', 'more', 'book'],
             ['weather', 'rain', 'snow'],
             ['yesterday', 'weather', 'snow'],
             ['forecast', 'tomorrow', 'rain', 'snow'],
             ['this', 'is', 'the', 'new', 'post'],
             ['this', 'is', 'about', 'more', 'machine', 'learning', 'post'],
             ['and', 'this', 'is', 'the', 'one', 'last', 'post', 'book']]
jobs_file = dataset_path + '/splitjobs/splitjobs/jobs2_partS.tsv'
jobs = pd.read_csv(jobs_file, sep='\t')
jobs = jobs[0:250]

tokens_arrays = jobs['Description'].apply(word_tokenize)
#print(type(tokens_arrays))

sentences = tokens_arrays.to_list()
#model = Word2Vec(sentences, min_count=1)
model = Word2Vec(sentences, min_count=1)

def sent_vectorizer(sent, model):
    sent_vec = []
    numw = 0
    for w in sent:
        try:
            if numw == 0:
                sent_vec = model.wv[w]
            else:
                sent_vec = np.add(sent_vec, model.wv[w])
            numw += 1
        except:
            pass

    return np.asarray(sent_vec) / numw


X = []
for sentence in sentences:
    X.append(sent_vectorizer(sentence, model))

#print("========================")
#print(X)

#print(model[model.wv.vocab])
#
#print(model.similarity('post', 'book'))
#print(model.most_similar(positive=['machine'], negative=[], topn=2))

NUM_CLUSTERS = 10
kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25, avoid_empty_clusters=True)
assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
print(assigned_clusters)

#for index, sentence in enumerate(sentences):
#    print(str(assigned_clusters[index]) + ":" + str(sentence))

kmeans = cluster.KMeans(n_clusters=NUM_CLUSTERS)
kmeans.fit(X)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# print("Cluster id labels for inputted data")
# print(labels)
# print("Centroids data")
# print(centroids)

# print(
#     "Score (Opposite of the value of X on the K-means objective which is Sum of distances of samples to their closest cluster center):")
# print(kmeans.score(X))

# silhouette_score = metrics.silhouette_score(X, labels, metric='euclidean')
#
# print("Silhouette_score: ")
# print(silhouette_score)

import matplotlib.pyplot as plt

from sklearn.manifold import TSNE

model = TSNE(n_components=2, random_state=0)
np.set_printoptions(suppress=True)

#Y = model.fit_transform(X)

#plt.scatter(Y[:, 0], Y[:, 1], c=assigned_clusters, s=290, alpha=.5)

for j in range(len(sentences)):
    #plt.annotate(assigned_clusters[j], xy=(Y[j][0], Y[j][1]), xytext=(0, 0), textcoords='offset points')
    print("%s %s" % (assigned_clusters[j], sentences[j]))

#plt.show()

jobs_categories = pd.DataFrame()
jobs_categories['Title'] = jobs.Title
jobs_categories['Clusters'] = pd.Series(assigned_clusters)
jobs_categories = jobs_categories.sort_values('Clusters')

jobs_categories.to_csv(results_path + '/JobsCategorization/word2vec_simple_on_description.csv', index=False)
