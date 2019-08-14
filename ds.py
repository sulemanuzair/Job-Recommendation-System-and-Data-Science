import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.get_backend()
matplotlib.use('TkAgg')


file_path = 'G:/Semester 8/FYP2/users/users_part.tsv'
# users = np.genfromtxt(fname=file_path, delimiter="\t", names=True, filling_values=1)
users = pd.read_csv(file_path, sep='\t')

# display more width and columns
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

#include all to include all columns in describe instead of just numeric columns
print (users.describe(include = 'all'))
print (users.ManagedOthers.unique())
print (users.shape)


# graph
# users.ManagedOthers.hist() #column='ManagedOthers')
# plt.show()

#graph
# users_who_managed_others = users.ManagedHowMany.loc[(users.ManagedHowMany > 0) & (users.ManagedHowMany < 100)]
# bucket_size = 10
# users_who_managed_others.hist(bins = range(min(users_who_managed_others), max(users_who_managed_others) + bucket_size, bucket_size))
# #plt.xscale('log')
# plt.xlabel('Number of Managed People')
# plt.ylabel('Number of Managers')
# plt.show()

users_with_cities_coordinates = users.loc[(users.CityLatitudeNew != 0) & (users.CityLongitudeNew != 0)]
from collections import Counter
# count the occurrences of each point
c = Counter(zip(users_with_cities_coordinates.CityLatitudeNew, users_with_cities_coordinates.CityLongitudeNew))
# create a list of the sizes, here multiplied by 10 for scale
s = [c[(xx,yy)] for xx,yy in zip(users_with_cities_coordinates.CityLatitudeNew, users_with_cities_coordinates.CityLongitudeNew)]

# plot it
#plt.scatter(users_with_cities_coordinates.CityLongitudeNew, users_with_cities_coordinates.CityLatitudeNew, s=s)
#plt.show()

print ('unique cities', users.City.unique().size)
print ('cities with known latitude and longitude', pd.unique(users.City.loc[(users.CityLongitudeNew != 0) & (users.CityLatitudeNew != 0)]).size)
print ('cities with not latitude and longitude in new file, but in prev file', pd.unique(users.City.loc[(users.CityLongitudeNew == 0) & (users.CityLatitudeNew == 0) & (users.CityLatitude != 0) & (users.CityLatitude != 0)]).size)

print ('Unique Contries: ', users.Country.unique())
#print (s)


# graph for countries
#users.Country.hist() #column='ManagedOthers')
#plt.show()

#users.Country.loc[(users.Country != 'US')].hist() #column='ManagedOthers')
#plt.show()

# graph for states
print("total states: ", users.loc[(users.Country == 'US')].State.unique().size)
print("states: ", users.loc[(users.Country == 'US')].State.unique())


# count the occurrences of each point
# checking for != 0 latitude as some entries has some issues, and/or do not exist in our states csv file
users_us = users.loc[(users.Country == 'US') & (users.StateLatitude != 0)]
print (users_us)
c_states = Counter(zip(users_us.StateLatitude, users_us.StateLongitude))
# create a list of the sizes, here multiplied by 10 for scale
s_states = [c_states[(xx,yy)] for xx,yy in zip(users_us.StateLatitude, users_us.StateLongitude)]

# plot it
#plt.scatter(users_us.StateLongitude, users_us.StateLatitude, s=s_states)
#plt.show()


#plt.show()
#users.loc[(users.Country == 'US')].State.hist(rwidth=0.5) #column='ManagedOthers')
#plt.show()

#print((users.loc[(users.Country == 'US')]).groupby('State').UserID.count())


# users.ManagedHowMany.loc[(users.ManagedHowMany > 0) & (users.ManagedHowMany < 100)]

# plt.scatter(users.CityLongitude, users.CityLatitude, marker = 'o', color='r', zorder=5, s=250)
# plt.show()
# users.boxplot()
# plt.show()

# Education
print (users.DegreeType.unique())

#users.DegreeType.value_counts().plot(kind='pie')
#users.DegreeType.hist()
#plt.show()


print ('different majors: ', users.Major.unique().size)
print ('different majors: ', users.Major.unique())
pd.set_option('display.max_rows', None)
print ('different majors: ', users.Major.value_counts())

#print ('rows having major majors: ', (users.Major == 'Finance' ).size )



# finance_users = (users.loc[(users.City == "Paramount")])
# #finance_users = users[(users.City.isnull())]
# finance_users = users.loc[users['Major'].isnull()]
#
# print (finance_users.Major)
# print (len(finance_users))



# plt.imshow()

# plt.interactive(False)

# plt.show()

# users.show()
# print(users.boxplot())


# print (users.TotalYearsExperience)
# print (users.columns)

# users['test'] = users.TotalYearsExperience / users.WorkHistoryCount
# summary = users.describe()
# print(summary)
# print (summary.loc['count'])
# print (users.loc[80:200, 'City'])
#
# print (users.dtype.names)
# print (np.mean(users['TotalYearsExperience']))
# print ("Median Experience : ", np.median(users['TotalYearsExperience']))
#
# print (np.mean(users['WorkHistoryCount']))
# print (np.mean(users['ManagedHowMany']))
#
# print(np.corrcoef(users['TotalYearsExperience'], users['WorkHistoryCount']))
# print(np.corrcoef(users['TotalYearsExperience'], users['ManagedHowMany']))
# print(np.corrcoef(users['WorkHistoryCount'], users['ManagedHowMany']))

# print(users.stats.describe)