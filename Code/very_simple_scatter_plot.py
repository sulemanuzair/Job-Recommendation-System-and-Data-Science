import matplotlib.pyplot as plt
from collections import Counter

x = [0, 1, 1, 2, 2, 2, 2, 2]
y = [0, 1, 2, 3, 3, 3, 3, 5]

c = Counter(zip(x, y))
# create a list of the sizes, here multiplied by 10 for scale
s = [10 * c[(xx, yy)] for xx, yy in zip(x, y)]

plt.scatter(x, y, s=s)
plt.show()
