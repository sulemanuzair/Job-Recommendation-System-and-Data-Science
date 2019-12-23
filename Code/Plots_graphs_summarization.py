import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Rectangle
matplotlib.get_backend()
matplotlib.use('TkAgg')
import dateutil.parser as parser
from matplotlib.font_manager import FontProperties
#changing font of matplotlib
from matplotlib import rcParams
import numpy as np

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Tahoma']

file_path = 'G:/Semester 8/FYP2/dataset/users/users_part.tsv'
users = pd.read_csv(file_path, sep='\t')

# display more width and columns
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)
cmap = plt.get_cmap('tab10')

users_who_managed_others = users.ManagedHowMany.loc[(users.ManagedHowMany > 0) & (users.ManagedHowMany < 100)]
bucket_size = 10
x = users_who_managed_others.hist(bins=range(min(users_who_managed_others), max(users_who_managed_others) + bucket_size, bucket_size), color=[cmap(0.1)], ec='black', width=5)
plt.xlabel('Managed these many employees', fontsize=16)
plt.ylabel('Number of Managers', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('How many employees have been managed by managers', fontsize=16)
plt.show()

# Old graph with longitude and latitude
# users_with_cities_coordinates = users.loc[(users.CityLatitudeNew != 0) & (users.CityLongitudeNew != 0)]
# from collections import Counter
# # count the occurrences of each point
# c = Counter(zip(users_with_cities_coordinates.CityLatitudeNew, users_with_cities_coordinates.CityLongitudeNew))
# # create a list of the sizes, here multiplied by 10 for scale
# s = [c[(xx,yy)] for xx,yy in zip(users_with_cities_coordinates.CityLatitudeNew, users_with_cities_coordinates.CityLongitudeNew)]
#
# # plot it
# plt.scatter(users_with_cities_coordinates.CityLongitudeNew, users_with_cities_coordinates.CityLatitudeNew, s=s)
# plt.show()
#
# print ('unique cities', users.City.unique().size)
# print ('cities with known latitude and longitude', pd.unique(users.City.loc[(users.CityLongitudeNew != 0) & (users.CityLatitudeNew != 0)]).size)
# print ('cities with not latitude and longitude in new file, but in prev file', pd.unique(users.City.loc[(users.CityLongitudeNew == 0) & (users.CityLatitudeNew == 0) & (users.CityLatitude != 0) & (users.CityLatitude != 0)]).size)

print('Unique Countries: ', users.Country.unique())
# Graph for users' countries
users.Country.hist(color=[cmap(0.8)], width=1)

plt.xlabel('Countries', fontsize=16)
plt.ylabel('Number of Users', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Country level users distribution', fontsize=16)
# legend
handles = [Rectangle((0, 0), 1, 1, color=cmap(0.8), ec='black')]
labels = ['United States of America']
plt.legend(handles, labels)
plt.show()
# Non US countries graph
users.Country.loc[(users.Country != 'US')].hist(color=[cmap(0.7)], width=0.8, ec='black', bins=np.arange(users.Country.unique().size)-0.5)
plt.xlabel('Countries', fontsize=16)
plt.ylabel('Number of Users', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
new_font = {'fontname': 'Helvetica'}
plt.title('Country level users distribution', fontsize=20, fontname='fantasy')
plt.show()

# Old graph for states
print("total states: ", users.loc[(users.Country == 'US')].State.unique().size)
print("states: ", users.loc[(users.Country == 'US')].State.unique())

# # count the occurrences of each point
# # checking for != 0 latitude as some entries has some issues, and/or do not exist in our states csv file
# users_us = users.loc[(users.Country == 'US') & (users.StateLatitude != 0)]
# print (users_us)
# c_states = Counter(zip(users_us.StateLatitude, users_us.StateLongitude))
# # create a list of the sizes, here multiplied by 10 for scale
# s_states = [c_states[(xx,yy)] for xx,yy in zip(users_us.StateLatitude, users_us.StateLongitude)]
#
# # plot it
# plt.scatter(users_us.StateLongitude, users_us.StateLatitude, s=s_states)
# plt.show()
print((users.loc[(users.Country == 'US')]).groupby('State').UserID.count())
# plt.scatter(users.CityLongitude, users.CityLatitude, marker='o', color='r', zorder=5, s=250)
# plt.show()

# Boxplots
users.WorkHistoryCount.to_frame().boxplot()
plt.show()
users.TotalYearsExperience.to_frame().boxplot()
plt.show()
users.ManagedHowMany.to_frame().boxplot()
plt.show()

# Education
print(users.DegreeType.unique())
rows = users.shape[0]
few_users = users[0:int(rows * 0.1)]
few_rows_count = few_users.shape[0]
# Degree Type pie chart
few_users.loc[few_users.DegreeType != 'None'].DegreeType.value_counts().plot(kind='pie')
plt.title("Distribution of Users' Degrees")
plt.ylabel('')
plt.show()
# Degree type better pie chart
cmap = plt.get_cmap('hsv')
none_values_count_degree_type = (few_users.DegreeType == 'None').sum()
none_values_percentage_degree_type = none_values_count_degree_type / few_rows_count * 100
degree_type_summarization = few_users.loc[few_users.DegreeType != 'None'].DegreeType.value_counts()

labels = degree_type_summarization.keys().to_list()
colors = [cmap(0.0), cmap(0.1), cmap(0.2), cmap(0.4), cmap(0.7), cmap(0.8)]
#colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', 'black', 'red', 'blue', 'green']

fig1, ax1 = plt.subplots()
ax1.pie(degree_type_summarization, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)

handles = [Rectangle((0, 0), 1, 1, color=c, ec='black') for c in ['Black']]
labels = ['None Values ' + str(round(none_values_percentage_degree_type, 2)) + '%']
ax1.legend(handles, labels, bbox_to_anchor=(1.1, 1.1), bbox_transform=ax1.transAxes)
# Inner circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')
plt.tight_layout()

plt.show()

#Some summarizations
print('Unique Majors Count: ', few_users.Major.unique().size)
print('Majors: ', few_users.Major.unique())
pd.set_option('display.max_rows', None)
print('Different majors: ', few_users.Major.value_counts())
print(few_users.Major.str.split(expand=True).stack().value_counts())
# Users' Major tokens summarization pie chart
major_tokens_summarization = few_users.loc[few_users.Major != 'Not Applicable'].Major.str.split(expand=True).stack().value_counts()
major_tokens_summarization.pop('and')
major_tokens_summarization[0:20].plot(kind='pie')
# Centre circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')
plt.tight_layout()
plt.show()
# Users' Majors summarization pie chart
few_users.loc[few_users.Major != 'Not Applicable'].Major.value_counts()[0:20].plot(kind='pie')
# Centre circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')
plt.tight_layout()
plt.show()
# Some summarizations
print('NA entries (on fraction of users) of major', few_users.Major.isna().sum())
print('NA entries (fraction of users) of graduation date', few_users.GraduationDate.isna().sum())
print(parser.parse(users.GraduationDate.loc[0]).year)
# Graduation year histogram
# Adding a new column in dataframe
users['GraduationYear'] = pd.DatetimeIndex(users.GraduationDate).year
bucket_size = 5
# users_who_managed_others.hist(bins = range(min(users_who_managed_others), max(users_who_managed_others) + bucket_size, bucket_size))
users.GraduationYear.hist(bins=15, color=[cmap(0.1)], ec='black', width=2)
plt.title('Users Graduation Year Distribution')
plt.show()
# Graduation Year Pie Chart
users['bins'] = pd.cut(users['GraduationYear'], bins=[1960, 1970, 1980, 1990, 2000, 2005, 2010, 2015, 2020], labels=["1960-70", "1970-80", "1980-90", "1990-2000", "2000-05", "2005-10", "2010-15", "2015-20"])
bins_count = users.groupby('bins').size()
bins_count.plot.pie(figsize=(8, 8))
plt.title('Users Graduation Year Distribution')
# Centre circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')
plt.tight_layout()
plt.show()

# Applying a condition on a column
print('rows having major majors: ', (users.Major == 'Finance').size)
# Some summarization
print("NA entries of WorkHistoryCount", users.WorkHistoryCount.isna().sum())
# Work History Count Histogram
users.WorkHistoryCount.hist(color=[cmap(0.1)], ec='black', width=0.6)
plt.title("Users Work History Count")
plt.show()
# Some summarization
print("NA entries of TotalYearsExperience", users.TotalYearsExperience.isna().sum())
# Experience Years Pie chart
users['bins'] = pd.cut(users['TotalYearsExperience'], bins=[0, 3, 5, 10, 15, 20, 25, 30, 200], labels=["0-3", "3-5", "5-10", "10-15", "15-20", "20-25", "25-30", ">30"])
bins_count = users.groupby('bins').size()
bins_count.plot.pie(figsize=(8, 8))
plt.title("Users Total Years Experience")
# Centre circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal')
plt.tight_layout()
plt.show()
# Years Experience Histogram
users.loc[(users.TotalYearsExperience < 50)].TotalYearsExperience.hist(color=[cmap(0.1)], ec='black', width=3)
plt.title("Users Total Years Experience")
plt.show()
# Some summarization
print(users.CurrentlyEmployed.unique())
print("NA entries of CurrentlyEmployed", users.CurrentlyEmployed.isna().sum())
# Currently Employed Pie chart
users.CurrentlyEmployed.value_counts().plot(kind='pie')
plt.title("Users Currently Employed")
plt.show()

# Some old code to set
# plt.imshow()
# plt.interactive(False)
# plt.show()
#
# users.show()
# print(users.boxplot())
#
# print (users.TotalYearsExperience)
# print (users.columns)
#
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
#
# print(users.stats.describe)