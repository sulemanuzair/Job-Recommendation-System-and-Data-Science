
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

from sklearn.preprocessing import LabelEncoder


users_with_clusters = 0
jobs_with_clusters = 0

scaler = preprocessing.MinMaxScaler()
      
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

for i in range(1):#(len(filesInputNames)):
    data =pd.read_csv(filesInputNames[i], sep='\t')   
    #le=preprocessing.LabelEncoder()
    #data = data.apply(le.fit_transform(data['']))
    
    
    
    
    #data = data.apply(LabelEncoder().fit_transform)
        
data_for_clustering = scaler.fit_transform(data)
data_for_clustering = pd.DataFrame(data_for_clustering)

rangeK = 50
K=range(1,rangeK)
distortion=[]
for k in K:
    Hclustering = KMeans(n_clusters=k)
    Hclustering.fit_predict(data_for_clustering)
    distortion.append(Hclustering.inertia_)
            
plt.plot(range(1,rangeK),distortion) 
plt.show()



