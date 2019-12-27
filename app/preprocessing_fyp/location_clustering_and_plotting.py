# =============================================================================
# import pandas as pd
# df = pd.DataFrame({'name': ['paris', 'berlin', 'london']})
# 
# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
# 
# from geopy.extra.rate_limiter import RateLimiter
# geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
# df['location'] = df['name'].apply(geocode)
# 
# df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
# 
# 
# =============================================================================


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



    
data =pd.read_csv('../splitjobs/splitjobs/jobs2_part.tsv', sep='\t')

#rt = data.join(df)

#print(rt .info())
#rt.to_csv("job11.csv", sep=',')

data1=data.iloc[:,11]
data2=data.iloc[:,12]
#print(d1)
from scipy.cluster.vq import kmeans2, whiten

#coordinates= np.array(coordinatesLocation)

#print(coordinates[:,0])
#print(coordinates[:,0])
#x, y = kmeans2(whiten(coordinates), 3, iter = 20)  

kmeans=KMeans(init='k-means++', n_clusters=7, n_init=10)
kmeans = kmeans.fit(data[['longitude','latitude']])
#print(y)
plt.scatter(data1, data2,c=kmeans.labels_)
plt.show()


