import pandas as pd



#import matplotlib.pyplot as plt
#help(plt.hist)
# values = [1,2,3,4,1,23,4,4,3,2,8,1]
# plt.hist(values, bins = 4)
# plt.show()




# matplotlib start
import matplotlib.pyplot as plt
year = [2000, 2005, 2010, 2015, 2020]
pop = [2, 3, 3.5, 5, 7]
pop = [1.0, 1.262, 1.650] + pop
year = [1800, 1850, 1900] + year
#plt.plot(year, pop)
plt.fill_between(year, pop, 0, color='blue')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population and its future')
plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B'])

#plt.scatter(year, pop)
plt.show()




# emulate your ex3.Severity.value_counts()
data = {'Low': 2, 'Medium': 4, 'High': 5}
df = pd.Series(data)

plt.bar(range(len(df)), df.values, align='center')
plt.xticks(range(len(df)), df.index.values, size='small')
plt.show()

# print ("IA library zaroor install hngi")
#
#
# import numpy as np
# import pandas as pd
#
# import matplotlib as plt
# # print ("na kro yaaaarr")
# #
# #
# arr = np.array([1,2,3])
# arr1 = np.array([[1,2,3],[1,2,3]])
# #
# # arr2 = arr/arr1
# # print (arr2)
# #
# #
# #
# # p = [1,2,3,4,5,6]
# # print (p)
# #
# #
# # hash = {"a":"b", "c":"d"}
# # print (hash['a'])
# print (type(arr1))
#
# print (arr1[1,1])
#




