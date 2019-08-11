import pandas as pd
from sklearn import preprocessing
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler    
from mpl_toolkits.mplot3d import Axes3D
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import csv
from bs4 import BeautifulSoup
import re, math
from collections import Counter
from nltk.stem.snowball import SnowballStemmer
import string
from nltk.tag import pos_tag
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.externals import joblib
                                                            
data =pd.read_csv("../users/users_part.tsv", sep='\t')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     WORD = re.compile(r'\w+')
     words = WORD.findall(text)
     return Counter(words)


def similarity_sentences(text1, text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine = get_cosine(vector1, vector2)       
    return cosine


users_with_clusters = 0
jobs_with_clusters = 0
user_history = 0
filesInputNames = [ 
                    '../splitjobs/splitjobs/jobs1_part.tsv', 
                    '../splitjobs/splitjobs/jobs2_part.tsv', 
                    '../splitjobs/splitjobs/jobs3_part.tsv', 
                    '../splitjobs/splitjobs/jobs4_part.tsv', 
                    '../splitjobs/splitjobs/jobs5_part.tsv', 
                    '../splitjobs/splitjobs/jobs6_part.tsv', 
                    '../splitjobs/splitjobs/jobs7_part.tsv', 
                    '../users/users_part.tsv',
                    '../user_history/user_history_part.tsv',
                    '../apps/apps_part.tsv'                     
        ]
scaler = preprocessing.MinMaxScaler()      

for i in range(len(filesInputNames)):
    data =pd.read_csv(filesInputNames[i], sep='\t')

    if(i >= 0 and i <= 6):
        if(i == 1):         
            synopses=[]
            titles=[]
  
            with open(filesInputNames[i-1], encoding="utf8") as csvfile:
                readCSV = csv.reader(csvfile, delimiter='\t')
                for row in readCSV:
                   titles.append(row[2])
             
            with open(filesInputNames[i-1], encoding="utf8") as csvfile:
                readCSV = csv.reader(csvfile, delimiter='\t')
                for row in readCSV:
                   t1 = row[2]
                   t2 = BeautifulSoup(row[3], "html.parser").get_text()
                   t3 = BeautifulSoup(row[4], "html.parser").get_text() 
                   cleantext =  t2 +  t3 
                   cleantext = cleantext.encode('ascii','ignore')
                   cleantext = t1 + str(cleantext)
                   synopses.append(cleantext)
                   
                   
            stopwords = nltk.corpus.stopwords.words('english')
            newStopWords = ['<br>','</br>','<p>','</p>','\b','\n','\r','\r\n','<b>','</b>','<a>','</a>','<strong>','</strong>',
                            '<BR>','</BR>','<span>','</span>','<B>','</B>','JOB REQUIREMENTS']
          
            stopwords.extend(newStopWords)
            stemmer = SnowballStemmer("english")
            
            
            def strip_proppers(text):
                tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent) if word.islower()]
                return "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
            
            def strip_proppers_POS(text):
                tagged = pos_tag(text.split())
                non_propernouns = [word for word,pos in tagged if pos != 'NNP' and pos != 'NNPS']
                return non_propernouns
            
            def tokenize_and_stem(text):
                tokenized_text = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
                removedStopWord = [word for word in tokenized_text if word not in stopwords] 
                filtered_tokens = []
                
                for token in removedStopWord:
                    if re.search('[a-zA-Z]', token):
                        filtered_tokens.append(token)
                stems = [stemmer.stem(t) for t in filtered_tokens]
                return stems  
                       
            def tokenize_only(text):
                tokenized_text = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
                removedStopWord = [word for word in tokenized_text if word not in stopwords] 
                filtered_tokens = []
                
                for token in removedStopWord:
                    if re.search('[a-zA-Z]', token):
                        filtered_tokens.append(token)
                return filtered_tokens
            
            totalvocab_stemmed = []
            totalvocab_tokenized = []
            for i in synopses:
                allwords_stemmed = tokenize_and_stem(i) 
                totalvocab_stemmed.extend(allwords_stemmed)
                
                allwords_tokenized = tokenize_only(i)
                totalvocab_tokenized.extend(allwords_tokenized)   
                    
            vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
                           
            tfidf_vectorizer = TfidfVectorizer(max_df=0.8, #max_features=200000,
                                             min_df=0.2, stop_words='english',
                                             use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))
            tfidf_matrix = tfidf_vectorizer.fit_transform(synopses) 
            terms = tfidf_vectorizer.get_feature_names()       
            dist = 1 - cosine_similarity(tfidf_matrix)
        
        
            rangeK = 50
            K=range(1,rangeK)
            distortion=[]
            for k in K:
                Hclustering = KMeans(n_clusters=k)
                Hclustering.fit_predict(tfidf_matrix)
                
                distortion.append(Hclustering.inertia_)
                        
            plt.plot(range(1,rangeK),distortion) 
            plt.show()
            
        
            num_clusters = 50
            km = KMeans(n_clusters=num_clusters)
            km.fit(tfidf_matrix)
            clusters = km.labels_.tolist()        
            
            joblib.dump(km,  'doc_cluster.pkl') 
            km = joblib.load('doc_cluster.pkl')
            clusters = km.labels_.tolist()
            films = { 'title': titles,  'synopsis': synopses, 'cluster': clusters }
            frame = pd.DataFrame(films, index = [clusters] , columns = ['title', 'cluster'])
            frame['cluster'].value_counts()
            
            data =pd.read_csv('../splitjobs/splitjobs/jobs1_part.tsv'  , sep='\t')
            data['Job_Description_Cluster'] = clusters[1:]
            data['Job_Location_Cluster'] = 0
            
            data['ClusterJob'] = data.apply(lambda row: row.Job_Description_Cluster + row.Job_Location_Cluster * num_clusters , axis=1)
            jobs_with_clusters = data
            
    if(i == 7):
        scaler=preprocessing.MinMaxScaler()

        data['State']=data['State'].fillna(value="Not")
        data['ZipCode']=data['ZipCode'].fillna(value=0)
        data['CurrentlyEmployed']=data['CurrentlyEmployed'].fillna(value="No")
        data['TotalYearsExperience']=data['TotalYearsExperience'].fillna(value=0.0)
        
        data['Major']=data['Major'].fillna(value="None")
        data['DegreeType'] = data['DegreeType'].map({'None': 0, "Bachelor's": 4, "Associate's": 3, "Master's": 5,
            "High School": 1, "PhD": 6, "Vocational": 2})
        data['CurrentlyEmployed'] = data['CurrentlyEmployed'].map({"Yes": 1, "No": 0})
        data['ManagedOthers'] = data['ManagedOthers'].map({"Yes": 1, "No": 0})
        data['Split'] = data['Split'].map({"Train": 0, "Test": 1})
        data['GraduationDate'] = pd.to_datetime(data.GraduationDate)

        data.drop(['GraduationDate'], axis = 1, inplace = True)
        le=preprocessing.LabelEncoder()
        
        v = TfidfVectorizer()
        x = v.fit_transform(data['Major'])
        data.drop(['Major'], axis = 1, inplace = True)
        
        major_cluster_preprocess=pd.DataFrame(x.toarray(), columns=v.get_feature_names())
        
        
        
        rangeK = 50
        K=range(1,rangeK)
        distortion=[]
        for k in K:
            Hclustering = KMeans(n_clusters=k)
            Hclustering.fit_predict(major_cluster_preprocess)
            distortion.append(Hclustering.inertia_)
                    
        plt.plot(range(1,rangeK),distortion) 
        plt.show()

        
        
        major_clusters = 30
        kmean=KMeans(n_clusters=major_clusters)
        major_cluster=kmean.fit_predict(major_cluster_preprocess)
        
        dataset = pd.DataFrame({'ClusterJob':major_cluster[:]})
        data['User_Major_Cluster'] = dataset[:]
        
        data_clustering_education_work = (data[['DegreeType', 'WorkHistoryCount', 'TotalYearsExperience','CurrentlyEmployed', 'ManagedOthers', 'ManagedHowMany' ]])
        scaled = preprocessing.scale(data_clustering_education_work)
        
        
        
        rangeK = 50
        K=range(1,rangeK)
        distortion=[]
        for k in K:
            Hclustering = KMeans(n_clusters=k)
            Hclustering.fit_predict(scaled)
            distortion.append(Hclustering.inertia_)
                    
        plt.plot(range(1,rangeK),distortion) 
        plt.show()




        kmean = KMeans(n_clusters = 20)
        education_work_clusters = kmean.fit_predict(scaled)
        
        data['User_Education_Work_Cluster'] = education_work_clusters[:]
        
        data['ClusterUser'] = data.apply(lambda row: row.User_Major_Cluster + row.User_Education_Work_Cluster *major_clusters , axis=1)
        users_with_clusters = data
        
    if(i == 8):
       user_history = data

    if (i == 9):
        data = data.set_index('UserID')
        
        data.to_csv('apps.csv')
        users_with_clusters.to_csv('UserClusters.tsv', sep ='\t')
        jobs_with_clusters.to_csv('JobsClusters.tsv', sep ='\t')
        
        users_with_clusters = users_with_clusters.set_index('UserID' )
        
        data = data.join(users_with_clusters, how = 'inner' , lsuffix='_left', rsuffix='_right')
        data = data.reset_index()
        data = data.set_index('JobID')
        
        jobs_with_clusters = jobs_with_clusters.set_index('JobID')
        jobs_with_clusters.to_csv('jc.csv')
        data.to_csv('jca.csv')
        
        data = data.join(jobs_with_clusters, how = 'inner', lsuffix = '_user', rsuffix = '_job')
        data = data.reset_index()
        data1 = data.groupby(['ClusterUser','ClusterJob']).size()
        
        data1 = data1.reset_index()
        data1.rename(columns = {0: 'frequency'}, inplace = True)
        
        
        data['frequency'] = 0
        for i in range(len(data1)):
            for j in range(len(data)):
                if data1['ClusterUser'].get(i) == data['ClusterUser'].get(j) and data1['ClusterJob'].get(i) == data['ClusterJob'].get(j):
                    data.set_value(j, 'frequency' , data1['frequency'].get(i))
        

        data['Similarity'] = np.random.uniform(0, 1, data.shape[0])
        data = data.sort_values(['ClusterUser', 'ClusterJob', 'Similarity'], ascending=[True, True, False])
         
        data = data.set_index('UserID')
        user_history = user_history.set_index('UserID' )
        data = data.join(user_history, how = 'inner' , rsuffix='_history')
        
        data = data.reset_index()
        data = data.sort_values(['ClusterUser', 'ClusterJob', 'Similarity'], ascending=[True, True, False])
        
        data_s = (data[['UserID', 'ClusterUser', 'JobID', 'ClusterJob' , 'Title', 'JobTitle']])
        uc_jc_pairs = (data[[ 'ClusterUser', 'ClusterJob' , 'Title', 'UserID', 'JobID']])
        
        index_1 = 0
        index_2_s = -1
        index_2_e = -1
        
        uc = -1
        jc = -1
        
        def findNextIndices():
            global uc
            global jc
            global index_1
            global index_2_s
            global index_2_e
            
            if (not (uc_jc_pairs.iloc[index_1].ClusterUser == uc and uc_jc_pairs.iloc[index_1].ClusterJob == jc)):
                tmp_uc = uc
                tmp_jc = jc
                uc = uc_jc_pairs.iloc[index_1].ClusterUser
                jc = uc_jc_pairs.iloc[index_1].ClusterJob
                
                count = 0
                index_1_copy = index_2_e + 1
                
                while (index_1_copy < len(data_s)):
                    if (data_s.iloc[index_1_copy].ClusterUser == uc and data_s.iloc[index_1_copy].ClusterJob == jc):
                        index_1_copy = index_1_copy + 1                        
                        count = count + 1
                    else:
                        break
               
                index_2_s = index_2_e 
                index_2_e = index_2_s + count
                            
            else:
                return 
        uc_jc_pairs['Similar'] = 0
        le = LabelEncoder()
        data_s = data_s[data_s['JobTitle'].notnull()]
        
        
        for i in range(len(uc_jc_pairs)):
            index_1 = i
            findNextIndices()
            
            difference = 0
            for k in range(index_2_s, index_2_e):
                difference = difference + (1 - similarity_sentences( uc_jc_pairs.iloc[i].Title , data_s.iloc[k].JobTitle))
            uc_jc_pairs.set_value(i, 'Similar' , difference)
                 
        uc_jc_pairs = uc_jc_pairs.sort_values(['ClusterUser', 'ClusterJob', 'Similar'],  ascending=[True, True, False])
        uc_jc_pairs.to_csv('ClusterWiseJobs.tsv', sep ='\t')
        
