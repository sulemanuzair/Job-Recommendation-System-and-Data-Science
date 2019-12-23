import matplotlib.pyplot as plt
import os
cmap = plt.get_cmap('tab20c')

year = [2000, 2005, 2010, 2015, 2020]
pop = [2, 3, 3.5, 5, 7]
pop = [1.0, 1.262, 1.650] + pop
year = [1800, 1850, 1900] + year

plt.xlabel('Year', fontsize=20)
plt.ylabel('Population', fontsize=20)
plt.title('World Population and its future', fontsize=20)
plt.yticks([0, 2, 4, 6, 8, 10],
           ['0', '2B', '4B', '6B', '8B', '10B'], fontsize=14)
plt.xticks(fontsize=14)
plt.tick_params(axis='y', which='both', labelleft=False, labelright=True)
plt.gca().yaxis.set_label_position("right")

plt.plot(year, pop, color='black')
plt.fill_between(year, pop, 0, color=cmap(0.05))
plt.scatter(year, pop, color=cmap(0))

# removing boundaries of plot
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

script_name = os.path.basename(__file__).split('.')[0]
plt.savefig('../Output/Graphs and Visualizations/' + script_name)
plt.show()
