
import csv
from collections import defaultdict
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler    
from mpl_toolkits.mplot3d import Axes3D
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd


yi=defaultdict(list)
arr=[]
longitude=[]
latitude=[]
coordinatesLocation=[]
t=0

with open('../splitjobs/splitjobs/jobs1_part.tsv', encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    for row in readCSV:
       #print(row[2])
       if(t>0):
           arr.append(row[5])
       t=t+1    
       #print arr

from geopy.geocoders import Nominatim
#from geopy.extra.rate_limiter import RateLimiter
geolocator = Nominatim(user_agent="myAPP",timeout=15)
#geocode=RateLimiter(geolocator.geocode,min_delay_seconds=1)

count = 0
for i in arr:
    
    if(count % 10 == 0):
        print ('count: ', count)
    count = count + 1
    
    #location = 0
    if i in yi:
        longitude.append(yi[i][0])
        latitude.append(yi[i][1])
    else:
         location = geolocator.geocode(i)
         
         if location:
             longitude.append(location.longitude)
             latitude.append(location.latitude)
             #coordinatesLocation.append((location.latitude, location.longitude))
             yi[i].append(location.longitude)
             yi[i].append(location.latitude)
         



df=pd.DataFrame({"longitude":longitude,
                "latitude":latitude})
    
#print(df)    

    
data =pd.read_csv('../splitjobs/splitjobs/jobs1_part.tsv', sep='\t')

rt = data.join(df)

#print(rt .info())
rt.to_csv("job11.csv", sep=',')

# =============================================================================
# d1=rt.iloc[:,11]
# d2=rt.iloc[:,12]
# #print(d1)
# from scipy.cluster.vq import kmeans2, whiten
# 
# #coordinates= np.array(coordinatesLocation)
# 
# #print(coordinates[:,0])
# #print(coordinates[:,0])
# #x, y = kmeans2(whiten(coordinates), 3, iter = 20)  
# 
# kmeans=KMeans(init='k-means++', n_clusters=3, n_init=10)
# kmeans = kmeans.fit(rt[['longitude','latitude']])
# #print(y)
# plt.scatter(d1, d2,c=kmeans.labels_)
# plt.show()
# 
# =============================================================================
