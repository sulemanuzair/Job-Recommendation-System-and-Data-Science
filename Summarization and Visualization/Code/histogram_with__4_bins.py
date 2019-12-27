# code could be improved, but didn't improve intentionally
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

# Plotting Histogram by dividing data into 4 bins
data = [1, 2, 3, 4, 1, 23, 4, 4, 3, 2, 8, 1]
frequencies, bins_center, patches = plt.hist(data, bins=4, rwidth=0.3, color='Yellow', ec='black')
plt.xlabel('Data', fontsize=16)
plt.ylabel('Frequency', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Histogram in 4 bins', fontsize=20)

cmap = plt.get_cmap('tab10')
Q1 = cmap(0.0)
Q2 = cmap(0.1)
Q3 = cmap(0.2)
Q4 = cmap(0.3)

patches[0].set_facecolor(Q1)
patches[1].set_facecolor(Q2)
patches[2].set_facecolor(Q3)
patches[3].set_facecolor(Q4)

handles = [Rectangle((0, 0), 1, 1, color=c, ec='black') for c in [Q1, Q2, Q3, Q4]]
labels = [str(bins_center[0]) + ' - ' + str(bins_center[1]),
          str(bins_center[1]) + ' - ' + str(bins_center[2]),
          str(bins_center[2]) + ' - ' + str(bins_center[3]),
          str(bins_center[3]) + ' - ' + str(bins_center[4])]
plt.legend(handles, labels, prop={'size': 15})

script_name = os.path.basename(__file__).split('.')[0]
plt.savefig('../Output/Graphs and Visualizations/' + script_name)
plt.show()
