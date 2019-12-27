from constants import *
import gensim
import pandas as pd
from nltk import word_tokenize

file_name = dataset_path + '/splitjobs/splitjobs/jobs2_partS.tsv'
jobs = pd.read_csv(file_name, sep='\t')


jobs['Title'].dropna(inplace=True)
tokens = jobs['Title'].apply(word_tokenize)
print (tokens)

array1 = tokens
model = gensim.models.Word2Vec(array1)#, size=150,window=10,min_count=2,workers=10)

model.train(array1, total_examples=len(array1), epochs=1)
model.save("word2vec.model")

print(len(model.wv.vocab))
print(model.wv.vocab)

w1 = "medical"
print("Most similar to {0}".format(w1), model.wv.most_similar(positive=w1))

print(model.wv.similarity(w1="assistant", w2="vice"))
print(model.wv.similarity(w1="assistant", w2="medical"))
print(model.wv.similarity(w1="assistant", w2="clerk"))
print(model.wv.similarity(w1="assistant", w2="sales"))
print(model.wv.similarity(w1="nurse", w2="medical"))
print(model.wv.similarity(w1="nurse", w2="engineer"))
print(model.wv.similarity(w1="mechanical", w2="engineer"))
print(model.wv.similarity(w1="software", w2="developer"))
print(model.wv.similarity(w1="sql", w2="developer"))

file_name = '../Reports/Jobs_Title_Tokens_Info_25percent.csv'
words = pd.read_csv(file_name)
words = words[['Word', 'Count', 'Type']]

seniority = words[words.Type==1]
