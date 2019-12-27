from sklearn import metrics
import gensim.models as g
import codecs
import pandas as pd

model = "doc2vec.bin"
test_docs = "data/test_docs.txt"

file_name = '../splitjobs/splitjobs/jobs2_partS.tsv'
jobs = pd.read_csv(file_name, sep='\t')
jobs = jobs[0:100]

# inference hyper-parameters
start_alpha = 0.1
infer_epoch = 50

# load model
m = g.Doc2Vec.load(model)
print ('vocab', m.wv.vocab)
print ('size', len(m.wv.vocab))
test_docs = [x.strip().split() for x in codecs.open(test_docs, "r", "utf-8").readlines()]

job_titles = jobs.Description.tolist()
test_docs = [x.strip().split() for x in job_titles]

X = []
for d in test_docs:
    X.append(m.infer_vector(d, alpha=start_alpha, steps=infer_epoch))
k = 10
print ('X', X)
from sklearn.cluster import Birch
brc = Birch(branching_factor=50, n_clusters=k, threshold=0.1, compute_labels=True)
brc.fit(X)
clusters = brc.predict(X)
labels = brc.labels_
print("Clusters: ")
print(clusters)

jobs['clusters'] = pd.Series(clusters)
jobs = jobs[['Title', 'clusters']]
jobs = jobs.sort_values('clusters')
jobs.to_csv('new_job_clusters.csv', index=False)
