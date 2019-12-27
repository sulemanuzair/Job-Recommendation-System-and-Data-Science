from gensim.models import KeyedVectors
import pandas as pd
import numpy as np
import string
from sklearn.decomposition import PCA
file_name = '../splitjobs/splitjobs/jobs2_partS.tsv'
jobs = pd.read_csv(file_name, sep='\t')
jobs = jobs[0:10000]

model = KeyedVectors.load("word2vec.model")
w2v_vectors = model.wv.vectors # here you load vectors for each word in your model
w2v_indices = {word: model.wv.vocab[word].index for word in model.wv.vocab} # here you load indices - with whom you can find an index of the particular word in your model

def vectorize(line):
    words = []
    for word in line: # line - iterable, for example list of tokens
        try:
            w2v_idx = w2v_indices[word]
        except KeyError: # if you does not have a vector for this word in your w2v model, continue
            continue
        words.append(w2v_vectors[w2v_idx])
        if words:
            words = np.asarray(words)
            min_vec = words.min(axis=0)
            max_vec = words.max(axis=0)
            return np.concatenate((min_vec, max_vec))
        if not words:
            return None

vectors = []
s = "Senior software enginner"
#print(vectorize(s))
for index, job in jobs.iterrows():
    vc = vectorize(job)
    vectors.append(vc)
    # if vc is not None:
    #     vectors.append(vc.reshape(1,-1))
    # else:
    #     vectors.append(None)
#vectors = vectors.reshape(1,-1)



#vectors = [[0] * 200 if v is None else v for v in vectors]

print ("vectors", vectors)

count = 0
present = []
new_vectors = []

for v in vectors:
    if v is None:
        present.append(0)
    else:
        present.append(1)
        new_vectors.append(v)

        count = count + 1
print (count)



from nltk.cluster import KMeansClusterer
import nltk
NUM_CLUSTERS=20
kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25,avoid_empty_clusters=True)
reduced_data = PCA(n_components=10).fit_transform(new_vectors) #
assigned_clusters = kclusterer.cluster(reduced_data, assign_clusters=True)
print (assigned_clusters)
print (len(assigned_clusters))


new_clusters = []
index = 0
for each in present:
    if each == 0:
        new_clusters.append(-1)
    else:
        new_clusters.append(assigned_clusters[index])
        index = index + 1

jobs['clusters'] = pd.Series(new_clusters)

# file_name_to_save = get_file_name_to_save(file_name)
# print (file_name_to_save)
jobs = jobs[['Title', 'clusters']]
jobs = jobs.sort_values('clusters')
jobs = jobs.loc[jobs['clusters'] != -1]
jobs.to_csv('new_job_clusters.csv', index=False)



# vectors = np.asarray(vectors, dtype=float)
# from sklearn.cluster import DBSCAN
# dbscan = DBSCAN(metric='cosine', eps=0.07, min_samples=3) # you can change these parameters, given just for example
# cluster_labels = dbscan.fit_predict(vectors.reshape(1,-1)) # where X - is your matrix, where each row corresponds to one document (line) from the docs, you need to cluster
# print (cluster_labels)


#print ("asd ads asdasd")

#X = model[model.wv.vocab]
# from nltk.cluster import KMeansClusterer
# import nltk
# NUM_CLUSTERS= 15
# kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25)
# assigned_clusters = kclusterer.cluster(X, assign_clusters=True)
# print (assigned_clusters)
# jobs['clusters'] = pd.Series(assigned_clusters)
# jobs = jobs[['Title', 'clusters']]
# jobs = jobs.sort_values('clusters')
# jobs.to_csv("do_it.csv")


