from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import pandas as pd
from collections import namedtuple

file_name = '../splitjobs/splitjobs/jobs2_partS.tsv'
jobs = pd.read_csv(file_name, sep='\t')
jobs = jobs[0:1000]

job_titles = jobs.Description.tolist()
test_docs = [x.strip().split() for x in job_titles]

docs = []
analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')
for i, text in enumerate(test_docs):
    words = text
    tags = [i]
    docs.append(analyzedDocument(words, tags))

model = Doc2Vec(docs, vector_size= 500, window = 200, min_count = 1, workers = 6)
#model.build_vocab(docs)

print ('vocab', model.wv.vocab)
print ('size', len(model.wv.vocab))

#model = Doc2Vec()#, vector_size=5, window=2, min_count=1, workers=4)

fname = "doc2vec.bin"#get_tmpfile("doc2vec.bin")
model.save(fname)
