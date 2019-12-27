# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 01:56:36 2019

@author: Haziq Farooq
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing
from constants import *

data = pd.read_csv(root_path + "/users/users_part.tsv", sep='\t')
scaler = preprocessing.MinMaxScaler()

data['State'] = data['State'].fillna(value="Not")
data['ZipCode'] = data['ZipCode'].fillna(value=0)
data['CurrentlyEmployed'] = data['CurrentlyEmployed'].fillna(value="No")
data['TotalYearsExperience'] = data['TotalYearsExperience'].fillna(value=0.0)
data['Major'] = data['Major'].fillna(value="None")
data['DegreeType'] = data['DegreeType'].map({'None': 0, "Bachelor's": 4, "Associate's": 3, "Master's": 5, "High School": 1, "PhD": 6, "Vocational": 2})
data['CurrentlyEmployed'] = data['CurrentlyEmployed'].map({"Yes": 1, "No": 0})
data['ManagedOthers'] = data['ManagedOthers'].map({"Yes": 1, "No": 0})
data['Split'] = data['Split'].map({"Train": 0, "Test": 1})
data['GraduationDate'] = pd.to_datetime(data.GraduationDate)
data.drop(['GraduationDate'], axis=1, inplace=True)

le = preprocessing.LabelEncoder()
v = TfidfVectorizer()
x = v.fit_transform(data['Major'])
data.drop(['Major'], axis=1, inplace=True)

major_cluster_preprocess=pd.DataFrame(x.toarray(), columns=v.get_feature_names())

kmean = KMeans(n_clusters=5)
major_cluster = kmean.fit_predict(major_cluster_preprocess)
major_clusters = pd.DataFrame({'ClusterJob':major_cluster[:]})
data['User_Major_Cluster'] = major_clusters

data_clustering_education_work = (data[['DegreeType', 'WorkHistoryCount', 'TotalYearsExperience','CurrentlyEmployed', 'ManagedOthers', 'ManagedHowMany' ]])
scaled = preprocessing.scale(data_clustering_education_work)
kmean = KMeans(n_clusters=7)
education_work_clusters = kmean.fit_predict(scaled)

print('Degree Major Clusters : ', major_clusters)
print('Education fields clusters: ', education_work_clusters)

data['User_Education_Work_Cluster'] = education_work_clusters[:]
data.to_csv(root_path + '/Results/FYPCodeResults/Users_Education_and_Major_Clustering.csv')