import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.get_backend()
matplotlib.use('TkAgg')


file_path = 'G:/Semester 8/FYP2/users/users_part.tsv'
#users = np.genfromtxt(fname=file_path, delimiter="\t", names=True, filling_values=1)
users = pd.read_csv(file_path, sep='\t')

# display more width and columns
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

#include all to include all columns in describe instead of just numeric columns
print (users.describe(include = 'all'))
print (users.ManagedOthers.unique())
print (users.shape)

#users.ManagedOthers.hist() #column='ManagedOthers')
#plt.show()
users_who_managed_others = users.ManagedHowMany.loc[(users.ManagedHowMany > 0) & (users.ManagedHowMany < 100)]
bucket_size = 10
users_who_managed_others.hist(bins = range(min(users_who_managed_others), max(users_who_managed_others) + bucket_size, bucket_size))
#plt.xscale('log')
plt.xlabel('Number of Managed People')
plt.ylabel('Number of Managers')
plt.show()

users.boxplot()
plt.show()



#plt.imshow()

#plt.interactive(False)

#plt.show()

#users.show()
#print(users.boxplot())


#print (users.TotalYearsExperience)
#print (users.columns)

#users['test'] = users.TotalYearsExperience / users.WorkHistoryCount
#summary = users.describe()
#print(summary)
#print (summary.loc['count'])
#print (users.loc[80:200, 'City'])
#
#print (users.dtype.names)
# print (np.mean(users['TotalYearsExperience']))
# print ("Median Experience : ", np.median(users['TotalYearsExperience']))
#
# print (np.mean(users['WorkHistoryCount']))
# print (np.mean(users['ManagedHowMany']))
#
# print(np.corrcoef(users['TotalYearsExperience'], users['WorkHistoryCount']))
# print(np.corrcoef(users['TotalYearsExperience'], users['ManagedHowMany']))
# print(np.corrcoef(users['WorkHistoryCount'], users['ManagedHowMany']))

#print(users.stats.describe)