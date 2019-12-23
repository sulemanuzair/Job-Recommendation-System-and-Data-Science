import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Rectangle

data = np.random.rayleigh(size=1000)*35
N, bins, patches = plt.hist(data, bins=30, ec='black')

cmap = plt.get_cmap('jet')
low = cmap(0.5)
medium = cmap(0.25)
high = cmap(0.8)


for i in range(0, 4):
    patches[i].set_facecolor(low)
for i in range(4, 11):
    patches[i].set_facecolor(medium)
for i in range(11, 30):
    patches[i].set_facecolor(high)

#create legend
handles = [Rectangle((0, 0), 1, 1, color=c, ec='black') for c in [low, medium, high]]
labels = ["low", "medium", "high"]
plt.legend(handles, labels)

plt.xlabel("Watt Hours", fontsize=16)
plt.ylabel("Households", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# removing boundaries of plot
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

script_name = os.path.basename(__file__).split('.')[0]
plt.savefig('../Output/Graphs and Visualizations/' + script_name)
plt.show()
