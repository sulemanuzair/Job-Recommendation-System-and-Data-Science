import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Rectangle
matplotlib.get_backend()
matplotlib.use('TkAgg')
import dateutil.parser as parser

file_path = 'G:/Semester 8/FYP2/dataset/users/users_part.tsv'
users = pd.read_csv(file_path, sep='\t')

# display more width and columns
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', None)

# Unique values
unique_managed_others = users.ManagedOthers.unique()
print('Managed Others Unique Values', unique_managed_others)

# Bar Graph
counts = users.ManagedOthers.value_counts()
output = plt.bar(counts.index, counts.values, ec='black', width=0.5)

cmap = plt.get_cmap('jet')
color1 = cmap(0.25)
color2 = cmap(0.75)

output[0].set_facecolor(color1)
output[1].set_facecolor(color2)

#create legend
handles = [Rectangle((0, 0), 1, 1, color=c, ec='black') for c in [color1, color2]]
labels = ["No", "Yes", ""]
plt.legend(handles, labels)

plt.xlabel("Managed Others", fontsize=16)
plt.ylabel("Frequency", fontsize=16)
plt.xticks(fontsize=14, rotation=45, rotation_mode="anchor", ha="center")
plt.yticks(fontsize=14)

# removing boundaries of plot
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.show()

# Histogram
N, bins, patches = plt.hist(users.ManagedOthers, align='mid', bins=2, ec='black', rwidth=0.5)
cmap = plt.get_cmap('jet')
color1 = cmap(0.25)
color2 = cmap(0.75)
print(N, len(bins), patches)

patches[0].set_facecolor(color1)
patches[1].set_facecolor(color2)

#create legend
handles = [Rectangle((0, 0), 1, 1, color=c, ec='black') for c in [color1, color2]]
labels = ["No", "Yes", ""]
plt.legend(handles, labels)

plt.xlabel("Managed Others", fontsize=16)
plt.ylabel("Frequency", fontsize=16)
plt.xticks(fontsize=14, rotation=45, rotation_mode="anchor", ha="center")
plt.yticks(fontsize=14)

# removing boundaries of plot
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.show()
